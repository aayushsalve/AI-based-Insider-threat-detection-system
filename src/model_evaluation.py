from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import joblib
import numpy as np

# Load dataset (replace with your actual data)
data = load_iris()
X = data.data
y = data.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n" + "="*60)
print("=== HYBRID MODEL EVALUATION ===")
print("="*60)

# Load trained models
iso_forest = joblib.load('Data/Models/isolation_forest_model.pkl')
random_forest = joblib.load('Data/Models/random_forest_model.pkl')

# Method 1: IsolationForest predictions
print("\n[1] IsolationForest (Primary Detector)")
iso_pred = iso_forest.predict(X_test)
iso_pred_binary = [1 if x == -1 else 0 for x in iso_pred]
iso_scores = iso_forest.score_samples(X_test)
iso_scores_norm = 1 / (1 + np.exp(iso_scores))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, iso_pred_binary))
print("\nClassification Report:")
print(classification_report(
    y_test, iso_pred_binary,
    target_names=['Normal', 'Anomaly']
))

# Method 2: RandomForest predictions
print("\n[2] RandomForest (Validation Layer)")
rf_pred = random_forest.predict(X_test)
rf_proba = random_forest.predict_proba(X_test)[:, 1]

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, rf_pred))
print("\nClassification Report:")
print(classification_report(
    y_test, rf_pred,
    target_names=['Normal', 'Anomaly']
))

# Method 3: Hybrid Approach (Weighted Voting)
print("\n[3] HYBRID MODEL (70% IsolationForest + 30% RandomForest)")
hybrid_scores = (iso_scores_norm * 0.7) + (rf_proba * 0.3)
hybrid_pred = [1 if score > 0.5 else 0 for score in hybrid_scores]

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, hybrid_pred))
print("\nClassification Report:")
print(classification_report(
    y_test, hybrid_pred,
    target_names=['Normal', 'Anomaly']
))

# Performance Metrics
print("\n" + "="*60)
print("=== PERFORMANCE COMPARISON ===")
print("="*60)
print(f"\nTotal Samples: {len(y_test)}")
print(f"Actual Anomalies: {sum(y_test)}")
print(f"\nIsolationForest Detected: {sum(iso_pred_binary)} anomalies")
print(f"RandomForest Detected: {sum(rf_pred)} anomalies")
print(f"Hybrid Model Detected: {sum(hybrid_pred)} anomalies")
