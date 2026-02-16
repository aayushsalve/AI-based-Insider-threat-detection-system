def create_features(df):
    features = df.groupby("user_id").agg({
        "login_hour": ["mean", "std"],
        "file_access_count": "sum",
        "sensitive_file_access": "sum"
    })

    # Flatten column names
    features.columns = [
        "login_hour_mean",
        "login_hour_std",
        "file_access_count_sum",
        "sensitive_file_access_sum"
    ]

    return features
