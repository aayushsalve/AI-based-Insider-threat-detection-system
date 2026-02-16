import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def preprocess_data(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.fillna(0, inplace=True)
    return df
