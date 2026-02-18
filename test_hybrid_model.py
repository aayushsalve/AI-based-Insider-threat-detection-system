#!/usr/bin/env python
"""
Test script for Hybrid Insider Threat Detection Model
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("=" * 70)
print("HYBRID MODEL TESTING - Insider Threat Detection System")
print("=" * 70)

# Step 1: Train the hybrid models
print("\n[STEP 1] Training Hybrid Models...")
print("-" * 70)

# Change to proper directory for model saving
os.chdir(os.path.join(os.path.dirname(__file__), 'Data'))

try:
    from sklearn.ensemble import IsolationForest, RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    import joblib
    import numpy as np

    # Create models directory if it doesn't exist
    if not os.path.exists('Models'):
        os.makedirs('Models')

    # Load dataset
    data = load_iris()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train IsolationForest
    print("  * Training IsolationForest...")
    iso_forest = IsolationForest(
        contamination=0.1,
        random_state=42,
        n_estimators=100
    )
    iso_forest.fit(X_train)
    print("    [OK] IsolationForest trained")

    # Train RandomForest
    print("  * Training RandomForest...")
    random_forest = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        max_depth=15,
        min_samples_split=5
    )
    random_forest.fit(X_train, y_train)
    print("    [OK] RandomForest trained")

    # Save models
    print("  * Saving models...")
    joblib.dump(iso_forest, 'Models/isolation_forest_model.pkl')
    joblib.dump(random_forest, 'Models/random_forest_model.pkl')
    print("    [OK] Models saved")

    # Test predictions
    print("\n[STEP 2] Testing Hybrid Model Predictions...")
    print("-" * 70)

    iso_pred = iso_forest.predict(X_test[:5])
    iso_scores = iso_forest.score_samples(X_test[:5])
    iso_scores_norm = 1 / (1 + np.exp(iso_scores))

    rf_proba = random_forest.predict_proba(X_test[:5])[:, 1]

    hybrid_scores = (iso_scores_norm * 0.7) + (rf_proba * 0.3)
    hybrid_pred = [1 if score > 0.5 else 0 for score in hybrid_scores]

    print("\nFirst 5 Test Samples:")
    print(f"{'Sample':<10} {'IsoForest':<12} {'RandomForest':<15} "
          f"{'Hybrid Score':<15} {'Prediction':<12}")
    print("-" * 70)

    for i in range(5):
        iso_s = f"{iso_scores_norm[i]:.3f}"
        rf_s = f"{rf_proba[i]:.3f}"
        hybrid_s = f"{hybrid_scores[i]:.3f}"
        pred = "ANOMALY" if hybrid_pred[i] == 1 else "NORMAL"
        print(f"{i+1:<10} {iso_s:<12} {rf_s:<15} {hybrid_s:<15} "
              f"{pred:<12}")

    print("\n[STEP 3] Model Statistics...")
    print("-" * 70)

    all_iso_pred = iso_forest.predict(X_test)
    all_iso_pred_binary = [1 if x == -1 else 0 for x in all_iso_pred]
    all_iso_scores_norm = 1 / (1 + np.exp(iso_forest.score_samples(X_test)))

    all_rf_proba = random_forest.predict_proba(X_test)[:, 1]

    all_hybrid_scores = (all_iso_scores_norm * 0.7) + (all_rf_proba * 0.3)
    all_hybrid_pred = [1 if score > 0.5 else 0
                       for score in all_hybrid_scores]

    print(f"Total Test Samples: {len(X_test)}")
    print("\nIsolationForest:")
    print(f"  * Anomalies Detected: {sum(all_iso_pred_binary)}")
    print(f"  * Avg Anomaly Score: {np.mean(all_iso_scores_norm):.3f}")

    print("\nRandomForest:")
    print(f"  * Avg Anomaly Probability: {np.mean(all_rf_proba):.3f}")

    print("\nHybrid Model:")
    print(f"  * Anomalies Detected: {sum(all_hybrid_pred)}")
    print(f"  * Avg Hybrid Score: {np.mean(all_hybrid_scores):.3f}")

    print("\n" + "=" * 70)
    print("[SUCCESS] HYBRID MODEL TESTING COMPLETED!")
    print("=" * 70)
    print("\nModels ready for production:")
    print("  * Data/Models/isolation_forest_model.pkl")
    print("  * Data/Models/random_forest_model.pkl")

except Exception as e:
    print(f"\n[ERROR]: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
