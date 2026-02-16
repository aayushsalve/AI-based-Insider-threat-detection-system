"""
Risk scoring module for insider threat detection.
Calculates risk scores based on detected anomalies and user behavior patterns.
"""

import pandas as pd
import numpy as np


def calculate_risk(
    data: pd.DataFrame,
    anomaly_scores: np.ndarray,
    threshold: float = 0.5
) -> pd.DataFrame:
    """
    Calculate risk scores for users based on anomaly detection results.

    Args:
        data: Preprocessed data DataFrame
        anomaly_scores: Array of anomaly scores from detection model
        threshold: Risk threshold for classification

    Returns:
        DataFrame with risk scores and classifications
    """
    risk_data = data.copy()
    risk_data['anomaly_score'] = anomaly_scores

    # Normalize scores to 0-1 range
    min_score = risk_data['anomaly_score'].min()
    max_score = risk_data['anomaly_score'].max()
    risk_data['risk_score'] = (
        (risk_data['anomaly_score'] - min_score) / (max_score - min_score)
    )

    # Classify risk level
    risk_data['risk_level'] = pd.cut(
        risk_data['risk_score'],
        bins=[0, 0.3, 0.7, 1.0],
        labels=['Low', 'Medium', 'High']
    )

    return risk_data


def aggregate_user_risk(
    risk_data: pd.DataFrame, user_column: str = 'user_id'
) -> pd.DataFrame:
    """
    Aggregate risk scores by user.

    Args:
        risk_data: DataFrame with risk scores
        user_column: Name of the user identifier column

    Returns:
        DataFrame with aggregated user risk metrics
    """
    user_risks = risk_data.groupby(user_column).agg({
        'risk_score': ['mean', 'max', 'std', 'count'],
        'anomaly_score': 'sum'
    }).reset_index()

    user_risks.columns = [
        '_'.join(col).strip('_') for col in user_risks.columns.values
    ]

    return user_risks
