import logging
import pandas as pd
from model_trainer import HybridModelTrainer
from config import PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def train_and_deploy():
    """Train final production model"""
    logger.info("="*60)
    logger.info("TRAINING PRODUCTION MODEL")
    logger.info("="*60)
    
    # Load balanced data
    X_df = pd.read_csv(PATHS["data"] / "features_balanced.csv")
    user_ids = X_df['user_id'].values
    X = X_df.drop('user_id', axis=1).values
    
    threat_labels = pd.read_csv(PATHS["data"] / "threat_labels_balanced.csv")
    y = threat_labels.set_index('user_id').loc[user_ids, 'is_threat'].values
    
    # Split data
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    logger.info(f"Training samples: {len(X_train)}")
    logger.info(f"Testing samples: {len(X_test)}")
    
    # Train model
    trainer = HybridModelTrainer()
    trainer.run(
        pd.DataFrame(X_train),
        pd.DataFrame(X_test),
        pd.Series(y_train),
        pd.Series(y_test)
    )
    
    logger.info("✅ Model training complete")
    logger.info("="*60)


if __name__ == "__main__":
    train_and_deploy()