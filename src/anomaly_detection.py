import pandas as pd
import joblib
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration constants
MODEL_PATHS = {
    'iso_forest': 'Data/Models/isolation_forest_model.pkl',
    'random_forest': 'Data/Models/random_forest_model.pkl'
}
ANOMALY_THRESHOLD = 0.5
ISO_FOREST_WEIGHT = 0.7
RANDOM_FOREST_WEIGHT = 0.3


class AnomalyDetector:
    """Enhanced anomaly detection with error handling and logging"""

    def __init__(self, model_paths=None):
        """Initialize detector with optional custom model paths"""
        self.model_paths = model_paths or MODEL_PATHS
        self.iso_forest = None
        self.random_forest = None
        self._load_models()

    def _load_models(self):
        """Load pre-trained models with error handling"""
        try:
            self.iso_forest = joblib.load(self.model_paths['iso_forest'])
            self.random_forest = joblib.load(self.model_paths['random_forest'])
            logger.info("Models loaded successfully")
        except FileNotFoundError as e:
            logger.error(f"Models not found: {e}")
            raise

    def _validate_input(self, features):
        """Validate input data"""
        if features is None or features.empty:
            raise ValueError("Input features cannot be empty")
        return features.select_dtypes(include=["int64", "float64"])

    def _calculate_iso_scores(self, numeric_features):
        """Calculate IsolationForest anomaly scores"""
        scores = self.iso_forest.score_samples(numeric_features)
        # Sigmoid normalization: convert to 0-1 range
        return 1 / (1 + np.exp(scores))

    def _calculate_rf_scores(self, numeric_features):
        """Calculate RandomForest anomaly probabilities"""
        probabilities = self.random_forest.predict_proba(numeric_features)
        return probabilities[:, 1]  # Probability of anomaly class

    def _compute_hybrid_scores(self, iso_scores, rf_scores):
        """Compute weighted hybrid anomaly scores"""
        return ((iso_scores * ISO_FOREST_WEIGHT) +
                (rf_scores * RANDOM_FOREST_WEIGHT))

    def _calculate_confidence(self, hybrid_scores):
        """Calculate confidence level (distance from 0.5 threshold)"""
        return np.abs(hybrid_scores - ANOMALY_THRESHOLD) * 2

    def detect_anomalies(self, features):
        """
        Hybrid anomaly detection using IsolationForest + RandomForest

        Args:
            features: DataFrame with feature columns

        Returns:
            DataFrame with anomaly predictions and confidence scores

        Raises:
            ValueError: If input is invalid
            FileNotFoundError: If models not found
        """
        try:
            # Validate and extract numeric features
            numeric_features = self._validate_input(features)

            # Calculate scores from both models
            iso_scores = self._calculate_iso_scores(numeric_features)
            rf_scores = self._calculate_rf_scores(numeric_features)

            # Compute hybrid scores
            hybrid_scores = self._compute_hybrid_scores(iso_scores, rf_scores)

            # Determine anomalies based on threshold
            anomalies = (hybrid_scores > ANOMALY_THRESHOLD).astype(int)

            # Calculate confidence
            confidence = self._calculate_confidence(hybrid_scores)

            # Add results to dataframe
            result = features.copy()
            result["anomaly"] = anomalies
            result["anomaly_score"] = hybrid_scores
            result["iso_score"] = iso_scores
            result["rf_score"] = rf_scores
            result["confidence"] = confidence

            num_anomalies = anomalies.sum()
            total_records = len(anomalies)
            logger.info(f"Detected {num_anomalies} anomalies out of "
                        f"{total_records} records")
            return result

        except Exception as e:
            logger.error(f"Anomaly detection failed: {e}")
            raise


def detect_anomalies_hybrid(features):
    """Wrapper for backward compatibility"""
    detector = AnomalyDetector()
    return detector.detect_anomalies(features)


def detect_anomalies(features):
    """Wrapper for backward compatibility"""
    return detect_anomalies_hybrid(features)


# Example test
if __name__ == "__main__":
    try:
        df = pd.read_csv("data/sample.csv")
        detector = AnomalyDetector()
        result = detector.detect_anomalies(df)
        print(result.head())
    except Exception as e:
        logger.error(f"Test failed: {e}")
