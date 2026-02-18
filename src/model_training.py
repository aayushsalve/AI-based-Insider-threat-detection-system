import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestClassifier


def train_hybrid_model(X_train, y_train):
    """
    Train hybrid anomaly detection model
    """
    # Train IsolationForest
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    iso_forest.fit(X_train)

    # Train RandomForest
    random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
    random_forest.fit(X_train, y_train)

    return iso_forest, random_forest


def predict_hybrid(iso_forest, random_forest, X_test):
    """
    Make predictions using hybrid model
    """
    iso_scores = iso_forest.score_samples(X_test)
    iso_scores_norm = 1 / (1 + np.exp(iso_scores))

    rf_proba = random_forest.predict_proba(X_test)[:, 1]

    hybrid_scores = (iso_scores_norm * 0.7) + (rf_proba * 0.3)
    return hybrid_scores
