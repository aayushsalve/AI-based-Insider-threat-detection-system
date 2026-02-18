import numpy as np
import pandas as pd
from config import RISK_WEIGHTS, RISK_THRESHOLDS
from logger import setup_logger

logger = setup_logger(__name__)


class RiskScorer:
    """Advanced risk scoring system"""

    def __init__(self):
        self.weights = RISK_WEIGHTS
        self.thresholds = RISK_THRESHOLDS

    def compute_hybrid_anomaly_score(self, iso_scores, svm_scores):
        iso_weight = 0.6
        svm_weight = 0.4

        def norm(a):
            mn, mx = float(a.min()), float(a.max())
            return (a - mn) / (mx - mn) if mx > mn else a * 0.0

        iso_n = norm(iso_scores)
        svm_n = norm(svm_scores)
        return (iso_weight * iso_n) + (svm_weight * svm_n)

    def compute_risk_scores(
        self, features_df, anomaly_scores, supervised_probs=None
    ):
        logger.info("Computing risk scores...")

        risk_df = features_df.copy()
        anomaly_scores = np.asarray(anomaly_scores, dtype=float)

        anom_weight = self.weights.get("anomaly", 0.4)
        sup_weight = self.weights.get("supervised", 0.3)

        anomaly_component = anomaly_scores * anom_weight * 10

        if supervised_probs is not None:
            supervised_probs = np.asarray(supervised_probs, dtype=float)
            supervised_component = supervised_probs * sup_weight * 10
        else:
            supervised_component = np.zeros(len(risk_df))

        if "sensitive_files_accessed" in risk_df.columns:
            max_sens = float(risk_df["sensitive_files_accessed"].max() or 1.0)
            sensitive_component = (
                (risk_df["sensitive_files_accessed"] / max_sens)
                * self.weights.get("sensitive_access", 0.2)
                * 10
            )
        else:
            sensitive_component = np.zeros(len(risk_df))

        if "failed_logins" in risk_df.columns:
            max_fails = float(risk_df["failed_logins"].max() or 1.0)
            login_component = (
                (risk_df["failed_logins"] / max_fails)
                * self.weights.get("login_anomalies", 0.1)
                * 10
            )
        else:
            login_component = np.zeros(len(risk_df))

        if "unique_locations" in risk_df.columns:
            max_locs = float(risk_df["unique_locations"].max() or 1.0)
            behavioral_component = (
                (risk_df["unique_locations"] / max_locs)
                * self.weights.get("behavioral", 0.1)
                * 10
            )
        else:
            behavioral_component = np.zeros(len(risk_df))

        risk_df["risk_score"] = (
            anomaly_component
            + supervised_component
            + sensitive_component
            + login_component
            + behavioral_component
        ).clip(0, 10)
        risk_df["anomaly_score"] = anomaly_scores
        risk_df["supervised_score"] = (
            supervised_probs if supervised_probs is not None else 0
        )

        risk_df["risk_level"] = pd.cut(
            risk_df["risk_score"],
            bins=[
                0,
                self.thresholds["medium"],
                self.thresholds["high"],
                self.thresholds["critical"],
                10,
            ],
            labels=["Low", "Medium", "High", "Critical"],
            include_lowest=True,
        )

        confidence_values = (np.abs(anomaly_scores - 0.5) * 2 * 100)
        risk_df["confidence"] = confidence_values.clip(0, 100)

        logger.info(f"✅ Computed risk scores for {len(risk_df)} users")
        return risk_df.sort_values("risk_score", ascending=False)

    def get_summary_stats(self, risk_df):
        return {
            "total_users": len(risk_df),
            "critical": int((risk_df["risk_level"] == "Critical").sum()),
            "high": int((risk_df["risk_level"] == "High").sum()),
            "medium": int((risk_df["risk_level"] == "Medium").sum()),
            "low": int((risk_df["risk_level"] == "Low").sum()),
            "avg_risk_score": float(risk_df["risk_score"].mean()),
            "max_risk_score": float(risk_df["risk_score"].max()),
            "min_risk_score": float(risk_df["risk_score"].min()),
            "std_risk_score": float(risk_df["risk_score"].std()),
        }
