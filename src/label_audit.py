import pandas as pd
from config import PATHS
from logger import setup_logger

logger = setup_logger(__name__)


def audit_labels():
    labels_path = PATHS["data"] / "threat_labels.csv"
    if not labels_path.exists():
        logger.error("threat_labels.csv not found")
        return

    df = pd.read_csv(labels_path)
    if "is_threat" not in df.columns:
        logger.error("Missing 'is_threat' column")
        return

    pos = int((df["is_threat"] == 1).sum())
    neg = int((df["is_threat"] == 0).sum())
    logger.info(f"Label audit: positives={pos}, negatives={neg}")

    if pos < 10:
        logger.warning("⚠️ Too few positives. Add real threat cases.")


if __name__ == "__main__":
    audit_labels()
