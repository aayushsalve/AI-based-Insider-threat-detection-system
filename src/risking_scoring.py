import pandas as pd


def compute_risk(features):
    """
    Compute risk scores using hybrid model results

    Combines:
    - Anomaly detection (70% IsolationForest + 30% RandomForest)
    - Sensitive file access patterns
    - User behavior confidence
    - Login attempt anomalies
    """
    # Validate input
    if features.empty:
        return features

    features = features.copy()

    # Get max sensitive access for normalization
    has_sensitive = "sensitive_file_access_sum" in features.columns
    max_sensitive = (features["sensitive_file_access_sum"].max()
                     if has_sensitive else 1)
    if max_sensitive == 0:
        max_sensitive = 1

    # Normalize anomaly scores to 0-1 range
    risk_score = pd.Series(0.0, index=features.index)

    # Component 1: Anomaly Score (40% weight)
    if "anomaly_score" in features.columns:
        anomaly_norm = features["anomaly_score"].clip(0, 1)
        risk_score += anomaly_norm * 4.0
    elif "anomaly" in features.columns:
        anomaly_norm = features["anomaly"].clip(0, 1)
        risk_score += anomaly_norm * 4.0

    # Component 2: Sensitive File Access (40% weight)
    if "sensitive_file_access_sum" in features.columns:
        sensitive_norm = (
            features["sensitive_file_access_sum"] / max_sensitive
        ).clip(0, 1)
        risk_score += sensitive_norm * 4.0

    # Component 3: Confidence Score (20% weight)
    if "confidence" in features.columns:
        confidence_norm = features["confidence"].clip(0, 1)
        risk_score += confidence_norm * 2.0

    # Cap at 10 and assign
    features["risk_score"] = risk_score.clip(upper=10)

    # Add risk level categorization
    features["risk_level"] = pd.cut(
        features["risk_score"],
        bins=[0, 3, 6, 8, 10],
        labels=["Low", "Medium", "High", "Critical"])

    return features.sort_values("risk_score", ascending=False)


def get_risk_summary(features):
    """Generate risk summary statistics"""
    risk_df = compute_risk(features)

    summary = {
        "total_users": len(risk_df),
        "critical_count": len(risk_df[risk_df["risk_level"] == "Critical"]),
        "high_count": len(risk_df[risk_df["risk_level"] == "High"]),
        "medium_count": len(risk_df[risk_df["risk_level"] == "Medium"]),
        "low_count": len(risk_df[risk_df["risk_level"] == "Low"]),
        "avg_risk_score": risk_df["risk_score"].mean(),
        "max_risk_score": risk_df["risk_score"].max()
    }

    return summary, risk_df
