from sklearn.ensemble import IsolationForest, RandomForestClassifier
import joblib

# Load and prepare data
# Replace with your actual insider threat dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n=== Training Hybrid Model ===")
print("Model 1: IsolationForest (Primary - Unsupervised Anomaly Detection)")

# Train IsolationForest model for anomaly detection
iso_forest = IsolationForest(
    contamination=0.1,  # Expect 10% anomalies (insider threats)
    random_state=42,
    n_estimators=100
)
iso_forest.fit(X_train)
print("✓ IsolationForest trained")

print("\nModel 2: RandomForest (Validation - Supervised Classification)")

# Train RandomForest model for validation/confirmation
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    max_depth=15,
    min_samples_split=5
)
random_forest.fit(X_train, y_train)
print("✓ RandomForest trained")

# Save both models
joblib.dump(iso_forest, 'Data/Models/isolation_forest_model.pkl')
joblib.dump(random_forest, 'Data/Models/random_forest_model.pkl')
print("\n✓ Hybrid models saved successfully!")
print("  - Data/Models/isolation_forest_model.pkl")
print("  - Data/Models/random_forest_model.pkl")
