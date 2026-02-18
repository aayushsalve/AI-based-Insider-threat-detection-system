import pandas as pd
import numpy as np


class EnhancedRiskScorer:
    """Advanced risk scoring with multiple factors"""

    def __init__(self):
        self.weights = {
            'anomaly': 0.40,
            'sensitive_access': 0.30,
            'login_anomalies': 0.20,
            'behavioral': 0.10
        }

    def compute_risk(self, features, anomaly_scores):
        """
        Compute multi-factor risk scores

        Returns:
            DataFrame with detailed risk metrics
        """
        risk_df = features.copy()

        # 1️⃣ ANOMALY COMPONENT (40%)
        risk_df['anomaly_score'] = np.clip(anomaly_scores, 0, 1)
        anomaly_component = (
            risk_df['anomaly_score'] * self.weights['anomaly'] * 10
        )

        # 2️⃣ SENSITIVE ACCESS COMPONENT (30%)
        if 'sensitive_files' in risk_df.columns:
            max_sens = risk_df['sensitive_files'].max() or 1
            sensitive_component = (
                (risk_df['sensitive_files'] / max_sens) *
                self.weights['sensitive_access'] * 10
            )
        else:
            sensitive_component = 0

        # 3️⃣ LOGIN ANOMALY COMPONENT (20%)
        if 'failed_logins' in risk_df.columns:
            max_fails = risk_df['failed_logins'].max() or 1
            login_component = (
                (risk_df['failed_logins'] / max_fails) *
                self.weights['login_anomalies'] * 10
            )
        else:
            login_component = 0

        # 4️⃣ BEHAVIORAL COMPONENT (10%)
        behavioral_component = 0  # Can add behavioral analysis here

        # Aggregate
        risk_df['risk_score'] = (
            anomaly_component + sensitive_component +
            login_component + behavioral_component
        ).clip(upper=10)

        # Categorize
        risk_df['risk_level'] = pd.cut(
            risk_df['risk_score'],
            bins=[0, 2, 4, 7, 10],
            labels=['Low', 'Medium', 'High', 'Critical'],
            include_lowest=True
        )

        # Confidence
        risk_df['confidence'] = np.abs(risk_df['anomaly_score'] - 0.5) * 2

        return risk_df.sort_values('risk_score', ascending=False)

    def get_summary(self, risk_df):
        """Generate executive summary"""
        return {
            'total_users': len(risk_df),
            'critical': len(risk_df[risk_df['risk_level'] == 'Critical']),
            'high': len(risk_df[risk_df['risk_level'] == 'High']),
            'avg_score': risk_df['risk_score'].mean(),
            'max_score': risk_df['risk_score'].max(),
            'std_dev': risk_df['risk_score'].std()
        }
