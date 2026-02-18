import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Configuration
CONFIG = {
    'data_dir': os.path.join(os.path.dirname(__file__), '../data'),
    'model_dir': os.path.join(os.path.dirname(__file__), '../Data/Models'),
    'anomaly_threshold': 0.5,
    'contamination': 0.1,
    'iso_forest_weight': 0.7,
    'random_forest_weight': 0.3
}


class DataPipeline:
    """Unified data loading and preprocessing"""

    def __init__(self, config=CONFIG):
        self.config = config
        os.makedirs(config['model_dir'], exist_ok=True)

    def load_all_data(self):
        """Load all required datasets"""
        try:
            users = pd.read_csv(f"{self.config['data_dir']}/users.csv")
            activities = pd.read_csv(
                f"{self.config['data_dir']}/activities.csv"
            )
            sensitive = pd.read_csv(
                f"{self.config['data_dir']}/sensitive_access.csv"
            )
            logins = pd.read_csv(
                f"{self.config['data_dir']}/login_attempts.csv"
            )
            labels = pd.read_csv(
                f"{self.config['data_dir']}/threat_labels.csv"
            )

            print(f"✅ Loaded {len(users)} users, {len(activities)} activities")
            return users, activities, sensitive, logins, labels
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data file missing: {e}")

    def extract_advanced_features(self, users, activities, sensitive, logins):
        """Extract comprehensive features"""
        features = []

        for user_id in users['user_id']:
            user_feat = {'user_id': user_id}

            # Activity patterns
            user_acts = activities[activities['user_id'] == user_id]
            user_feat['total_activities'] = len(user_acts)
            failed_acts = user_acts[user_acts['status'] == 'failed']
            user_feat['failed_activities'] = len(failed_acts)
            download_acts = user_acts[
                user_acts['activity_type'] == 'data_download'
            ]
            user_feat['downloads_gb'] = (
                download_acts['data_volume_mb'].sum() / 1024
            )

            # Sensitive file access
            user_sens = sensitive[sensitive['user_id'] == user_id]
            user_feat['sensitive_files'] = len(user_sens)
            after_hours = user_sens[user_sens['is_after_hours']]
            user_feat['after_hours_access'] = len(after_hours)
            anomalous = user_sens[user_sens['is_anomalous'] is True]
            user_feat['sensitive_anomalies'] = len(anomalous)

            # Login anomalies
            user_log = logins[logins['user_id'] == user_id]
            failed_logins = user_log[
                user_log['login_status'] == 'failed'
            ].shape[0]
            user_feat['failed_logins'] = failed_logins
            user_feat['unique_ips'] = user_log['source_ip'].nunique()
            user_feat['unique_locations'] = user_log['location'].nunique()

            # Behavioral indicators
            variance = (
                user_acts.groupby('timestamp').size().std()
                if len(user_acts) > 0 else 0
            )
            user_feat['activity_variance'] = variance
            user_feat['risk_score_baseline'] = 0  # Will be computed later

            features.append(user_feat)

        return pd.DataFrame(features).fillna(0)

    def preprocess_features(self, features):
        """Normalize and prepare features"""
        df = features.copy()
        user_ids = df['user_id'].values
        X = df.drop('user_id', axis=1)

        # Scale numerics
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Save scaler for later use
        scaler_path = f"{self.config['model_dir']}/scaler.pkl"
        joblib.dump(scaler, scaler_path)
        feature_cols_path = (
            f"{self.config['model_dir']}/feature_columns.pkl"
        )
        joblib.dump(X.columns.tolist(), feature_cols_path)

        return X_scaled, scaler, user_ids
