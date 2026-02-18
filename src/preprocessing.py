import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_and_preprocess():
    df = pd.read_csv("data/simulate_activity.csv")

    # Fill missing values
    df.fillna(0, inplace=True)

    # Encode categorical columns
    cat_cols = ['user_id', 'activity_type', 'file_access_type',
                'location', 'device_id']
    encoder = LabelEncoder()

    for col in cat_cols:
        if col in df.columns:
            df[col] = encoder.fit_transform(df[col].astype(str))

    # Select features for ML
    features = df[
        ['user_id',
         'activity_type',
         'file_access_type',
         'login_hour',
         'successful_activity',
         'is_sensitive_file_access']
    ]

    # Scale features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    return df, features_scaled
