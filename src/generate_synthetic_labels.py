import logging
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from data_pipeline import DataPipeline
from config import PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_synthetic_data():
    """Generate synthetic threat users (features + labels)"""
    logger.info("Loading data...")
    pipeline = DataPipeline()
    result = pipeline.run()

    X = result['features_scaled']
    user_ids = np.array(result['user_ids'])

    # Load original labels
    threat_labels = pd.read_csv(PATHS["data"] / "threat_labels.csv")
    y = threat_labels.set_index('user_id').loc[user_ids, 'is_threat'].values

    logger.info(f"Original distribution: {np.bincount(y)}")

    # Apply SMOTE to balance to 40% positives
    smote = SMOTE(sampling_strategy=0.4, random_state=42, k_neighbors=3)
    X_bal, y_bal = smote.fit_resample(X, y)

    logger.info(f"Balanced distribution: {np.bincount(y_bal)}")
    num_synthetic = len(X_bal) - len(X)
    logger.info(
        f"New size: {len(X_bal)} (added {num_synthetic} synthetic samples)"
    )

    # Create user IDs for synthetic samples
    synthetic_user_ids = list(user_ids)
    for i in range(len(X_bal) - len(X)):
        synthetic_user_ids.append(f"USER_SYN_{i:04d}")

    # Save balanced features
    feature_cols = result['feature_columns']
    X_bal_df = pd.DataFrame(X_bal, columns=feature_cols)
    X_bal_df['user_id'] = synthetic_user_ids
    X_bal_df.to_csv(PATHS["data"] / "features_balanced.csv", index=False)

    # Save balanced labels
    balanced_labels = pd.DataFrame({
        'user_id': synthetic_user_ids,
        'is_threat': y_bal
    })
    output_path = PATHS["data"] / "threat_labels_balanced.csv"
    balanced_labels.to_csv(output_path, index=False)

    logger.info("✅ Saved balanced features & labels")


if __name__ == "__main__":
    generate_synthetic_data()
