from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Directory configurations
PATHS = {
    'data': PROJECT_ROOT / 'data',
    'raw': PROJECT_ROOT / 'data' / 'raw',
    'models': PROJECT_ROOT / 'Data' / 'Models',
    'reports': PROJECT_ROOT / 'reports',
    'logs': PROJECT_ROOT / 'logs'
}

# Create directories if they don't exist
for p in PATHS.values():
    p.mkdir(parents=True, exist_ok=True)

# Model configurations
MODEL_CONFIG = {
    "isolation_forest": {
        "contamination": 0.1,
        "n_estimators": 200,
        "random_state": 42
    },
    "one_class_svm": {"nu": 0.1, "kernel": "rbf", "gamma": "scale"},
    "random_forest": {
        "n_estimators": 300,
        "random_state": 42,
        "class_weight": "balanced",
        "min_threshold": 0.45,  # Changed from 0.67
        "top_k": 10,
        "calibration": "isotonic",
        "calibration_cv": 3,
        "model": "xgboost",
        "use_smote": True,
        "smote_k_neighbors": 3
    },
}

# Risk scoring weights
RISK_WEIGHTS = {
    'anomaly': 0.4,
    'sensitive_access': 0.3,
    'login_anomalies': 0.2,
    'behavioral': 0.1,
    'supervised': 0.3
}

# Risk thresholds
RISK_THRESHOLDS = {
    'critical': 8.0,
    'high': 6.0,
    'medium': 4.0,
    'low': 0.0
}

# Logging
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}
