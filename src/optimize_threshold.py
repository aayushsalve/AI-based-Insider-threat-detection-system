import logging
import pandas as pd
import numpy as np
from sklearn.metrics import precision_recall_curve, roc_auc_score
from model_trainer import HybridModelTrainer
from config import PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def optimize_threshold():
    """Find optimal threshold using ROC-AUC and F1"""
    logger.info("="*60)
    logger.info("OPTIMIZING DECISION THRESHOLD")
    logger.info("="*60)

    # Load balanced data
    X_df = pd.read_csv(PATHS["data"] / "features_balanced.csv")
    user_ids = X_df['user_id'].values
    X = X_df.drop('user_id', axis=1).values

    threat_labels = pd.read_csv(PATHS["data"] / "threat_labels_balanced.csv")
    y = threat_labels.set_index('user_id').loc[user_ids, 'is_threat'].values

    # Train on full dataset
    trainer = HybridModelTrainer()
    trainer.run(pd.DataFrame(X), pd.DataFrame(X[:len(X)//5]),
                pd.Series(y), pd.Series(y[:len(y)//5]))
    
    y_prob = trainer.get_supervised_probs(pd.DataFrame(X))
    
    # Calculate PR curve
    precision, recall, thresholds = precision_recall_curve(y, y_prob)
    
    # Find optimal threshold
    f1_scores = 2 * (precision * recall) / (precision + recall + 1e-10)
    optimal_idx = np.argmax(f1_scores)
    optimal_threshold = (thresholds[optimal_idx]
                         if optimal_idx < len(thresholds) else 0.5)
    
    # Calculate AUC
    auc = roc_auc_score(y, y_prob)
    
    logger.info("\nOptimal Threshold Analysis:")
    logger.info(f"  Optimal Threshold: {optimal_threshold:.4f}")
    logger.info(f"  Max F1 Score: {f1_scores[optimal_idx]:.4f}")
    logger.info(f"  Precision @ optimal: {precision[optimal_idx]:.4f}")
    logger.info(f"  Recall @ optimal: {recall[optimal_idx]:.4f}")
    logger.info(f"  ROC-AUC: {auc:.4f}")
    
    # Save threshold
    threshold_config = pd.DataFrame({
        'metric': ['optimal_threshold', 'f1_score', 'auc',
                   'precision', 'recall'],
        'value': [optimal_threshold, f1_scores[optimal_idx], auc,
                  precision[optimal_idx], recall[optimal_idx]]
    })
    
    threshold_config.to_csv(PATHS["reports"] / "optimal_threshold.csv",
                            index=False)
    logger.info("\n✅ Threshold config saved")
    logger.info("="*60)


if __name__ == "__main__":
    optimize_threshold()
