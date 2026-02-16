import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(features):

    # Use only numeric columns for ML
    numeric_features = features.select_dtypes(include=["int64", "float64"])

    # Create model
    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    # Train model
    model.fit(numeric_features)

    # Predict anomalies
    predictions = model.predict(numeric_features)

    # Convert: -1 -> anomaly (1), 1 -> normal (0)
    features["anomaly"] = [1 if x == -1 else 0 for x in predictions]

    return features


# Example test (optional)
if __name__ == "__main__":

    # Load sample data
    df = pd.read_csv("data/sample.csv")  # change path if needed

    # Detect anomalies
    result = detect_anomalies(df)

    # Show output
    print(result.head())
