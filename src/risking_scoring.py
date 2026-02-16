def compute_risk(features):
    """
    Compute risk scores using hybrid model results
    
    Combines:
    - Anomaly detection (70% IsolationForest + 30% RandomForest)
    - Sensitive file access patterns
    - User behavior confidence
    """
    # Get max sensitive access for normalization
    max_sensitive = features["sensitive_file_access_sum"].max() if "sensitive_file_access_sum" in features.columns else 1
    if max_sensitive == 0:
        max_sensitive = 1
    
    # Calculate risk score (0-10 scale)
    risk_score = 0
    
    # Component 1: Anomaly Score (40% weight)
    if "anomaly_score" in features.columns:
        risk_score += features["anomaly_score"] * 4.0
    elif "anomaly" in features.columns:
        risk_score += features["anomaly"] * 4.0
    
    # Component 2: Sensitive File Access (40% weight)
    if "sensitive_file_access_sum" in features.columns:
        risk_score += (features["sensitive_file_access_sum"] / max_sensitive) * 4.0
    
    # Component 3: Confidence Score (20% weight)
    if "confidence" in features.columns:
        risk_score += features["confidence"] * 2.0
    
    features["risk_score"] = risk_score.clip(upper=10)  # Cap at 10
    
    return features.sort_values("risk_score", ascending=False)
