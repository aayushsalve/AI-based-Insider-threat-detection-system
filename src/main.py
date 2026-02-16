def calculate_risk(df):
    """
    Calculate risk scores for each user based on anomaly indicators.

    Args:
        df: DataFrame with anomaly detection results

    Returns:
        DataFrame with added 'risk_score' column
    """
    # Initialize risk score
    df['risk_score'] = 0

    # Add points for various risk factors
    if 'is_anomaly' in df.columns:
        df.loc[df['is_anomaly'], 'risk_score'] += 3

    if 'anomaly_score' in df.columns:
        df['risk_score'] += (df['anomaly_score'] * 10).astype(int)

    # Cap risk score at 10
    df['risk_score'] = df['risk_score'].clip(upper=10)

    return df
