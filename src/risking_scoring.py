def compute_risk(features):
    max_sensitive = features["sensitive_file_access_sum"].max()

    features["risk_score"] = (
        features["anomaly"] * 0.7 +
        (features["sensitive_file_access_sum"] / max_sensitive) * 0.3
    )

    return features.sort_values("risk_score", ascending=False)
