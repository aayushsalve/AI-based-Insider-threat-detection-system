import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from config import PATHS
from logger import setup_logger

logger = setup_logger(__name__)


class DataPipeline:
    """Complete data loading and feature engineering"""

    def __init__(self):
        self.scaler = None
        self.feature_columns = None

    def load_data(self):
        logger.info("Loading data files...")

        candidates = {
            "users": ["users.csv"],
            "activities": [
                "activities.csv",
                "simulate_activity.csv",
                "simulated_activity.csv",
            ],
            "sensitive_access": [
                "sensitive_access.csv",
                "simulate_file_access.csv",
            ],
            "login_attempts": ["login_attempts.csv", "simulate_logins.csv"],
            "threat_labels": ["threat_labels.csv"],
        }

        loaded_data = {}
        for key, names in candidates.items():
            found = None
            for filename in names:
                fp = PATHS["data"] / filename
                if fp.exists():
                    found = fp
                    break
            if found:
                loaded_data[key] = pd.read_csv(found)
                logger.info(f"✅ Loaded {key}: {len(loaded_data[key])} rows")
            else:
                logger.warning(f"⚠️ File not found for {key}: {names}")

        return loaded_data

    def extract_features(
        self, user_id, user_data, activities, sensitive_access, login_attempts
    ):
        logger.info("Extracting features...")

        if "timestamp" in activities.columns:
            activities = activities.copy()
            activities["timestamp"] = pd.to_datetime(
                activities["timestamp"], errors="coerce"
            )

        if "timestamp" in login_attempts.columns:
            login_attempts = login_attempts.copy()
            login_attempts["timestamp"] = pd.to_datetime(
                login_attempts["timestamp"], errors="coerce"
            )

        # Calculate activity frequency
        days_diff = (
            (activities["timestamp"].max() - activities["timestamp"].min())
            .days + 1
        )
        activity_freq = len(activities) / max(1, days_diff)

        # Extract hour data for reuse
        activity_hours = activities["timestamp"].dt.hour.dropna()
        has_hours = len(activity_hours) > 0

        features = {
            # Basic user features
            "user_id": user_id,
            "total_activities": len(activities),
            "failed_activities": int((activities["status"] == "failed").sum()),
            "downloads_count": int(
                (activities["activity_type"] == "data_download").sum()
            ),
            "activity_frequency": activity_freq,
            "activity_hour_mean": (
                float(activity_hours.mean()) if has_hours else 0
            ),
            "activity_hour_std": (
                float(activity_hours.std()) if has_hours else 0
            ),
            "activity_after_hours_rate": float(
                ((activity_hours < 7) | (activity_hours > 19)).mean()
            ) if has_hours else 0,
            "activity_weekend_rate": float(
                (activities["timestamp"].dt.weekday >= 5).mean()
            ),
            "sensitive_files_accessed": len(sensitive_access),
            "after_hours_access": int(
                sensitive_access["is_after_hours"].astype(bool).sum()
            ),
            "sensitive_after_hours_rate": (
                user_data["after_hours_access"]
                / max(1, len(sensitive_access))
            ),
            "total_logins": len(login_attempts),
            "failed_logins": int(
                (login_attempts.get("login_status", "") == "failed").sum()
            ),
            "failed_login_rate": (
                user_data["failed_logins"] / max(1, len(login_attempts))
            ),
            "unique_ips": (
                user_data["source_ip"].nunique()
                if "source_ip" in user_data.columns
                else 0
            ),
            "unique_locations": (
                user_data["location"].nunique()
                if "location" in user_data.columns
                else 0
            ),
            # NEW: Command execution patterns
            "command_execution_count": len(
                activities[activities["action_type"] == "execute_command"]
            ),
            "script_execution_count": len(
                activities[
                    activities["action_type"].str.contains(
                        "script", case=False, na=False
                    )
                ]
            ),
            # NEW: File operations frequency
            "file_copy_count": len(
                activities[activities["action_type"] == "copy_file"]
            ),
            "file_delete_count": len(
                activities[activities["action_type"] == "delete_file"]
            ),
            "file_modify_count": len(
                activities[activities["action_type"] == "modify_file"]
            ),
            # NEW: Permission changes
            "permission_changes": len(
                activities[activities["action_type"] == "change_permissions"]
            ),
            # NEW: Unusual access patterns
            "access_to_admin_resources": len(
                sensitive_access[sensitive_access["resource_type"] == "admin"]
            ),
            "access_to_system_files": len(
                sensitive_access[sensitive_access["resource_type"] == "system"]
            ),
            # NEW: Login velocity (logins per hour)
            "login_velocity": (
                len(login_attempts)
                / max(login_attempts["timestamp"].dt.hour.nunique(), 1)
            ),
            # NEW: Failed login clustering
            "failed_login_clustering": (
                len(login_attempts[login_attempts["status"] == "failed"])
                / max(len(login_attempts), 1)
            ),
        }

        return features

    def preprocess_features(self, features_df):
        logger.info("Preprocessing features...")

        df = features_df.copy()
        user_ids = df["user_id"].values
        X = df.drop("user_id", axis=1)
        self.feature_columns = X.columns.tolist()

        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)

        joblib.dump(self.scaler, PATHS["models"] / "scaler.pkl")
        feature_cols_path = PATHS["models"] / "feature_columns.pkl"
        joblib.dump(self.feature_columns, feature_cols_path)

        return X_scaled, user_ids

    def run(self):
        """Run the data pipeline"""
        logger.info("=" * 70)
        logger.info("STARTING DATA PIPELINE")
        logger.info("=" * 70)

        data = self.load_data()

        # Load balanced labels instead of original
        threat_labels_path = (
            PATHS["data"] / "threat_labels_balanced.csv"
        )
        threat_labels = pd.read_csv(threat_labels_path)

        features_df = self.extract_features(
            data["users"],
            data["activities"],
            data["sensitive_access"],
            data["login_attempts"],
        )
        X_scaled, user_ids = self.preprocess_features(features_df)

        logger.info("=" * 70)
        logger.info("✅ DATA PIPELINE COMPLETE")
        logger.info("=" * 70)

        return {
            "features_raw": features_df,
            "features_scaled": X_scaled,
            "user_ids": user_ids,
            "feature_columns": self.feature_columns,
            "raw_data": data,
            "threat_labels": threat_labels,
        }


if __name__ == "__main__":
    logger.info("=" * 70)
    logger.info("✅ DATA PIPELINE COMPLETE")
    logger.info("=" * 70)
