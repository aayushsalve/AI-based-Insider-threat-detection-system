import sys
import os
import pandas as pd
from anomaly_detection import AnomalyDetector  # type: ignore

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Load data
df = pd.read_csv('data/sample.csv')

# Run detection
detector = AnomalyDetector()
result = detector.detect_anomalies(df)

# Display results
print("\n" + "="*80)
print("ANOMALY DETECTION RESULTS")
print("="*80)
print(f"\nTotal Records: {len(result)}")
print(f"Anomalies Found: {result['anomaly'].sum()}")
print(f"Detection Rate: {(result['anomaly'].sum()/len(result)*100):.2f}%")

print("\n--- TOP ANOMALIES ---")
anomalies = result[result['anomaly'] == 1].sort_values(
    'anomaly_score', ascending=False
)
print(anomalies[['anomaly_score', 'iso_score', 'rf_score',
                 'confidence']].head(10))

print("\n--- STATISTICS ---")
print(result[['anomaly_score', 'confidence']].describe())

# Save results
result.to_csv('results/anomaly_results.csv', index=False)
print("\n✓ Results saved to results/anomaly_results.csv")
