import pandas as pd
import joblib
import numpy as np


def detect_anomalies_hybrid(features):
    """
    Hybrid anomaly detection using IsolationForest + RandomForest
    
    Args:
        features: DataFrame with feature columns
        
    Returns:
        DataFrame with anomaly predictions and confidence scores
    """
    # Use only numeric columns for ML
    numeric_features = features.select_dtypes(include=["int64", "float64"])
    
    # Load trained models
    try:
        iso_forest = joblib.load('Data/Models/isolation_forest_model.pkl')
        random_forest = joblib.load('Data/Models/random_forest_model.pkl')
    except:
        print("Models not found. Run test_hybrid_model.py first.")
        return features
    
    # Method 1: IsolationForest (Primary - Unsupervised)
    iso_predictions = iso_forest.predict(numeric_features)
    iso_anomalies = [1 if x == -1 else 0 for x in iso_predictions]
    iso_scores = iso_forest.score_samples(numeric_features)
    iso_scores_normalized = 1 / (1 + np.exp(iso_scores))  # Sigmoid normalization
    
    # Method 2: RandomForest (Validation - Supervised)
    rf_probabilities = random_forest.predict_proba(numeric_features)
    rf_anomaly_prob = rf_probabilities[:, 1]  # Probability of anomaly class
    
    # Hybrid Decision (Weighted Voting)
    # IsolationForest: 70% weight (primary detector)
    # RandomForest: 30% weight (validation)
    hybrid_scores = (iso_scores_normalized * 0.7) + (rf_anomaly_prob * 0.3)
    
    # Threshold for anomaly: >0.5
    hybrid_anomalies = [1 if score > 0.5 else 0 for score in hybrid_scores]
    
    # Add results to dataframe
    features["anomaly"] = hybrid_anomalies
    features["anomaly_score"] = hybrid_scores
    features["iso_score"] = iso_scores_normalized
    features["rf_score"] = rf_anomaly_prob
    features["confidence"] = np.abs(hybrid_scores - 0.5) * 2  # Confidence: 0-1
    
    return features


def detect_anomalies(features):
    """Wrapper for backward compatibility"""
    return detect_anomalies_hybrid(features)


# Example test (optional)
if __name__ == "__main__":

    # Load sample data
    df = pd.read_csv("data/sample.csv")  # change path if needed

    # Detect anomalies
    result = detect_anomalies(df)

    # Show output
    print(result.head())
