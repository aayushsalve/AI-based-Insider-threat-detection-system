import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_recall_curve,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.svm import OneClassSVM
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import HistGradientBoostingClassifier
from config import PATHS, MODEL_CONFIG
from logger import setup_logger
from datetime import datetime

logger = setup_logger(__name__)

try:
    from imblearn.over_sampling import SMOTE
except Exception:
    SMOTE = None


class HybridModelTrainer:
    """Train hybrid anomaly detection model"""

    def __init__(self):
        self.iso_forest = None
        self.oc_svm = None
        self.random_forest = None
        self.supervised = None
        self.calibrated_rf = None

    def _log_class_balance(self, y, label="labels"):
        values, counts = np.unique(y, return_counts=True)
        dist = {int(v): int(c) for v, c in zip(values, counts)}
        total = int(np.sum(counts))
        logger.info(f"{label} distribution: {dist} (total={total})")

    def _balance_data(self, X, y):
        cfg = MODEL_CONFIG.get("random_forest", {})
        use_smote = bool(cfg.get("use_smote", True)) and SMOTE is not None

        values, counts = np.unique(y, return_counts=True)
        if len(values) < 2:
            return X, y

        min_count = counts.min()
        max_count = counts.max()
        ratio = min_count / max(1, max_count)
        if ratio >= 0.2:
            return X, y

        if use_smote:
            k = int(cfg.get("smote_k_neighbors", 3))
            logger.info(f"Applying SMOTE (k={k}) for class imbalance...")
            sm = SMOTE(k_neighbors=k, random_state=42)
            return sm.fit_resample(X, y)

        logger.info("Applying random oversampling for class imbalance...")
        min_class = values[np.argmin(counts)]
        min_idx = np.where(y == min_class)[0]
        add_count = max_count - min_count
        add_idx = np.random.choice(min_idx, size=add_count, replace=True)
        X_new = np.vstack([X, X[add_idx]])
        y_new = np.concatenate([y, y[add_idx]])
        return X_new, y_new

    def train_isolation_forest(self, X_train):
        logger.info("Training IsolationForest...")
        config = MODEL_CONFIG["isolation_forest"]
        self.iso_forest = IsolationForest(
            contamination=config["contamination"],
            n_estimators=config["n_estimators"],
            random_state=config["random_state"],
            n_jobs=-1
        )
        self.iso_forest.fit(X_train)
        logger.info("✅ IsolationForest trained")
        return self.iso_forest

    def train_one_class_svm(self, X_train):
        logger.info("Training One-Class SVM...")
        default_config = {"nu": 0.1, "kernel": "rbf", "gamma": "scale"}
        config = MODEL_CONFIG.get("one_class_svm", default_config)
        self.oc_svm = OneClassSVM(
            nu=config.get("nu", 0.1),
            kernel=config.get("kernel", "rbf"),
            gamma=config.get("gamma", "scale"),
        )
        self.oc_svm.fit(X_train)
        logger.info("✅ One-Class SVM trained")
        return self.oc_svm

    def train_random_forest(self, X_train, y_train):
        logger.info("Training RandomForest...")
        config = MODEL_CONFIG.get("random_forest", {})
        self.random_forest = RandomForestClassifier(
            n_estimators=config.get("n_estimators", 300),
            random_state=config.get("random_state", 42),
            class_weight=config.get("class_weight", "balanced"),
            n_jobs=-1
        )
        self.random_forest.fit(X_train, y_train)
        logger.info("✅ RandomForest trained")
        return self.random_forest

    def train_supervised(self, X_train, y_train):
        cfg = MODEL_CONFIG.get("random_forest", {})
        model_type = cfg.get("model", "random_forest")

        if model_type == "xgboost":
            try:
                from xgboost import XGBClassifier
                logger.info("Training XGBoost...")
                self.supervised = XGBClassifier(
                    n_estimators=300,
                    learning_rate=0.05,
                    max_depth=6,
                    subsample=0.9,
                    colsample_bytree=0.9,
                    random_state=42,
                    eval_metric="logloss"
                )
                self.supervised.fit(X_train, y_train)
                logger.info("✅ XGBoost trained")
                return self.supervised
            except Exception:
                logger.warning(
                    "XGBoost not available; falling back to RandomForest."
                )

        if model_type == "hist_gb":
            logger.info("Training HistGradientBoosting...")
            self.supervised = HistGradientBoostingClassifier(random_state=42)
            self.supervised.fit(X_train, y_train)
            logger.info("✅ HistGradientBoosting trained")
            return self.supervised

        self.supervised = self.train_random_forest(X_train, y_train)
        return self.supervised

    def calibrate(self, X_train, y_train):
        cfg = MODEL_CONFIG.get("random_forest", {})
        method = cfg.get("calibration", "isotonic")
        cv = int(cfg.get("calibration_cv", 3))
        logger.info(f"Calibrating probabilities: method={method}, cv={cv}")
        self.calibrated_rf = CalibratedClassifierCV(
            self.supervised, method=method, cv=cv
        )
        self.calibrated_rf.fit(X_train, y_train)
        logger.info("✅ Calibrated model trained")

    def get_supervised_probs(self, X):
        if self.calibrated_rf is not None:
            return self.calibrated_rf.predict_proba(X)[:, 1]
        return self.supervised.predict_proba(X)[:, 1]

    def save_models(self):
        logger.info("Saving models...")
        joblib.dump(self.iso_forest, PATHS["models"] / "iso_forest_model.pkl")
        joblib.dump(self.oc_svm, PATHS["models"] / "one_class_svm_model.pkl")
        joblib.dump(self.supervised, PATHS["models"] / "supervised_model.pkl")
        if self.calibrated_rf is not None:
            model_path = PATHS["models"] / "calibrated_supervised.pkl"
            joblib.dump(self.calibrated_rf, model_path)
        logger.info(f"✅ Models saved to {PATHS['models']}")

    def _save_threshold_report(self, y_true, y_prob):
        if y_true is None or y_prob is None:
            return

        thresholds = np.linspace(0, 1, 101)
        rows = []

        top_k = int(MODEL_CONFIG.get("random_forest", {}).get("top_k", 10))
        order = np.argsort(-y_prob)
        if len(y_true) >= top_k:
            p_at_k = float(np.mean(y_true[order[:top_k]]))
        else:
            p_at_k = 0.0

        for t in thresholds:
            y_pred = (y_prob >= t).astype(int)
            precision = precision_score(y_true, y_pred, zero_division=0)
            recall = recall_score(y_true, y_pred, zero_division=0)
            f1 = f1_score(y_true, y_pred, zero_division=0)
            alerts = int(y_pred.sum())
            avg_score_alerts = (
                float(y_prob[y_pred == 1].mean())
                if alerts > 0
                else 0.0
            )

            rows.append({
                "threshold": float(t),
                "precision": float(precision),
                "recall": float(recall),
                "f1": float(f1),
                "alerts": alerts,
                "avg_score_alerts": avg_score_alerts,
                f"precision_at_{top_k}": p_at_k
            })

        df = pd.DataFrame(rows)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = PATHS["reports"] / f"threshold_report_{ts}.csv"
        df.to_csv(out_path, index=False)

        best_f1 = df.loc[df["f1"].idxmax()]
        logger.info(f"Threshold report saved: {out_path}")
        threshold_val = best_f1['threshold']
        f1_val = best_f1['f1']
        logger.info(
            f"Best F1 threshold: {threshold_val:.3f} (F1={f1_val:.3f})"
        )

    def evaluate(self, X_test, y_test):
        logger.info("Evaluating models...")

        y_prob = self.get_supervised_probs(X_test)
        self._save_threshold_report(y_test, y_prob)

        precision, recall, thresholds = precision_recall_curve(y_test, y_prob)
        f1 = (2 * precision * recall) / (precision + recall + 1e-9)
        best_idx = int(np.nanargmax(f1))
        auto_threshold = (
            thresholds[best_idx]
            if best_idx < len(thresholds)
            else 0.5
        )

        min_threshold = MODEL_CONFIG.get("random_forest", {}).get(
            "min_threshold", 0.15
        )
        threshold = max(float(auto_threshold), float(min_threshold))

        y_pred = (y_prob >= threshold).astype(int)

        k = int(MODEL_CONFIG.get("random_forest", {}).get("top_k", 10))
        k = max(1, min(k, len(y_prob)))
        topk_idx = np.argsort(y_prob)[::-1][:k]
        precision_at_k = float(np.mean(y_test[topk_idx]))

        logger.info("\n" + "=" * 60)
        logger.info(
            f"CLASSIFICATION REPORT (auto={auto_threshold:.3f}, "
            f"min={min_threshold:.3f}, used={threshold:.3f})"
        )
        logger.info("=" * 60)
        report = classification_report(y_test, y_pred, zero_division=0)
        logger.info("\n" + report)
        logger.info(f"Precision@K (K={k}): {precision_at_k:.3f}")

        logger.info("\n" + "=" * 60)
        logger.info("CONFUSION MATRIX")
        logger.info("=" * 60)
        cm = confusion_matrix(y_test, y_pred)
        logger.info(f"\n{cm}")

        return {
            "predictions": y_pred,
            "confusion_matrix": cm,
            "threshold": float(threshold)
        }

    def run(self, X_train, X_test, y_train, y_test):
        logger.info("=" * 70)
        logger.info("STARTING MODEL TRAINING")
        logger.info("=" * 70)

        self._log_class_balance(y_train, "train labels")
        self._log_class_balance(y_test, "test labels")

        X_train, y_train = self._balance_data(X_train, y_train)

        self.train_isolation_forest(X_train)
        self.train_one_class_svm(X_train)
        self.train_supervised(X_train, y_train)
        self.calibrate(X_train, y_train)

        results = self.evaluate(X_test, y_test)
        self.save_models()

        logger.info("=" * 70)
        logger.info("✅ MODEL TRAINING COMPLETE")
        logger.info("=" * 70)

        return results
