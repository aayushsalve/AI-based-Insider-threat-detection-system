import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (precision_score, recall_score, f1_score,
                             confusion_matrix)
from model_trainer import HybridModelTrainer
from config import PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def evaluate_kfold():
    logger.info("Loading balanced data...")

    # Load balanced features
    X_df = pd.read_csv(PATHS["data"] / "features_balanced.csv")
    user_ids = X_df['user_id'].values
    X = X_df.drop('user_id', axis=1).values

    # Load balanced labels
    threat_labels = pd.read_csv(PATHS["data"] / "threat_labels_balanced.csv")
    y = threat_labels.set_index('user_id').loc[user_ids, 'is_threat'].values

    logger.info(f"Data shape: X={X.shape}, y={y.shape}")
    logger.info(f"Label distribution: {np.bincount(y)}")

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = {"precision": [], "recall": [], "f1": [], "cm": []}

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        logger.info(f"\n{'='*60}")
        logger.info(f"FOLD {fold+1}/5")
        logger.info(f"{'='*60}")

        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        logger.info(f"Train: {len(y_train)} | Test: {len(y_test)}")
        logger.info(
            f"Train positives: {y_train.sum()} | "
            f"Test positives: {y_test.sum()}"
        )

        trainer = HybridModelTrainer()
        trainer.run(
            pd.DataFrame(X_train),
            pd.DataFrame(X_test),
            pd.Series(y_train),
            pd.Series(y_test)
        )
        y_prob = trainer.get_supervised_probs(pd.DataFrame(X_test))
        y_pred = (y_prob >= 0.45).astype(int)

        p = precision_score(y_test, y_pred, zero_division=0)
        r = recall_score(y_test, y_pred, zero_division=0)
        f = f1_score(y_test, y_pred, zero_division=0)
        cm = confusion_matrix(y_test, y_pred)

        scores["precision"].append(p)
        scores["recall"].append(r)
        scores["f1"].append(f)
        scores["cm"].append(cm)

        logger.info(f"Precision: {p:.3f} | Recall: {r:.3f} | F1: {f:.3f}")
        logger.info(f"CM:\n{cm}")

    logger.info(f"\n{'='*60}")
    logger.info("CROSS-VALIDATION RESULTS")
    logger.info(f"{'='*60}")
    avg_prec = np.mean(scores['precision'])
    std_prec = np.std(scores['precision'])
    logger.info(f"Avg Precision: {avg_prec:.3f} ± {std_prec:.3f}")
    avg_rec = np.mean(scores['recall'])
    std_rec = np.std(scores['recall'])
    logger.info(f"Avg Recall: {avg_rec:.3f} ± {std_rec:.3f}")
    avg_f1 = np.mean(scores['f1'])
    std_f1 = np.std(scores['f1'])
    logger.info(f"Avg F1: {avg_f1:.3f} ± {std_f1:.3f}")


if __name__ == "__main__":
    evaluate_kfold()
