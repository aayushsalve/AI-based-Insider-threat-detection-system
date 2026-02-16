# utils.py

def encode_categorical_columns(df, columns):
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    for col in columns:
        df[col] = label_encoder.fit_transform(df[col])
    return df
