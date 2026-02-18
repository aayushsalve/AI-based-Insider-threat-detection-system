import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(features_df):
    """
    Preprocess features for model training
    """
    df = features_df.copy()

    # Handle missing values
    df = df.fillna(0)

    # Separate features and user_id
    user_ids = df['user_id']
    X = df.drop('user_id', axis=1)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
    return X_scaled_df, scaler, user_ids
