import numpy as np
from sklearn.model_selection import train_test_split
from data_pipeline import DataPipeline
from model_trainer import HybridModelTrainer
from logger import setup_logger

logger = setup_logger(__name__)


def main():
    pipeline = DataPipeline()
    pipeline_result = pipeline.run()

    X_scaled = pipeline_result["features_scaled"]
    labels_df = pipeline_result["raw_data"].get("threat_labels")

    if labels_df is not None and "is_threat" in labels_df.columns:
        y = labels_df["is_threat"].values
    else:
        logger.warning("⚠️ No labels found, using random labels for demo.")
        y = np.random.randint(0, 2, len(X_scaled))

    stratify_param = y if len(set(y)) > 1 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=stratify_param
    )

    trainer = HybridModelTrainer()
    trainer.run(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
