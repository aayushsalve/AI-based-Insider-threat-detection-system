import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest, RandomForestClassifier
import numpy as np
import os

# Create directories
os.makedirs('Data/Models', exist_ok=True)

# Load sample data
df = pd.read_csv('data/sample.csv')

# Train IsolationForest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(df)
joblib.dump(iso_forest, 'Data/Models/isolation_forest_model.pkl')
print("✓ IsolationForest model trained")

# Train RandomForest (create dummy labels for demo)
y = np.random.randint(0, 2, len(df))
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(df, y)
joblib.dump(rf, 'Data/Models/random_forest_model.pkl')
print("✓ RandomForest model trained")

# Load models
iso_forest = joblib.load('Data/Models/isolation_forest_model.pkl')
rf = joblib.load('Data/Models/random_forest_model.pkl')

# Detect anomalies
anomalies = iso_forest.predict(df)
anomalies = anomalies.reshape(-1, 1)

# Create a DataFrame
df_anomalies = pd.DataFrame({
    'login_attempts': df['login_attempts'],
    'files_accessed': df['files_accessed'],
    'confidence': anomalies[:, 0]  # Extract first column only
})

# Save the DataFrame
df_anomalies.to_csv('data/anomalies.csv', index=False)

print("Models loaded successfully")
print(f"Detected {len(anomalies)} anomalies out of {len(df)} records")
