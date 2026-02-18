import sys
import os
import pandas as pd

from data_generation import save_synthetic_data
from feature_engineering import extract_features
from data_preprocessing import preprocess_data
from model_training import train_hybrid_model
from risking_scoring import compute_risk

sys.path.insert(0, os.path.dirname(__file__))


def run_pipeline():
    """
    Execute complete insider threat detection pipeline
    """
    print("=" * 70)
    print("INSIDER THREAT DETECTION PIPELINE")
    print("=" * 70)

    # Step 1: Generate data
    print("\n[1/5] Generating synthetic data...")
    save_synthetic_data("../data")

    # Step 2: Load data
    print("[2/5] Loading data...")
    users = pd.read_csv("../data/users.csv")
    activities = pd.read_csv("../data/activities.csv")
    sensitive = pd.read_csv("../data/sensitive_access.csv")
    login = pd.read_csv("../data/login_attempts.csv")
    labels = pd.read_csv("../data/threat_labels.csv")

    # Step 3: Extract features
    print("[3/5] Extracting features...")
    features = extract_features(activities, sensitive, login, users)

    # Step 4: Preprocess
    print("[4/5] Preprocessing data...")
    X_scaled, scaler, user_ids = preprocess_data(features)

    # Step 5: Train models
    print("[5/5] Training models...")
    iso_forest, random_forest = train_hybrid_model(
        X_scaled, labels['is_threat']
    )

    # Compute risk scores
    print("\n[RESULTS] Computing risk scores...")
    risk_results = compute_risk(features.merge(labels, on='user_id'))

    high_risk_count = len(
        risk_results[risk_results['risk_level'] == 'High']
    )
    critical_count = len(
        risk_results[risk_results['risk_level'] == 'Critical']
    )
    print(f"\nHigh-risk users: {high_risk_count}")
    print(f"Critical users: {critical_count}")

    print("\n[SUCCESS] Pipeline completed!")


if __name__ == "__main__":
    run_pipeline()
