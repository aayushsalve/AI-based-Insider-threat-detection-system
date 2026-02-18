import pandas as pd
from config import PATHS
from logger import setup_logger

logger = setup_logger(__name__)

DATASETS = {
    "users.csv": "users",
    "activities.csv": "activities",
    "sensitive_access.csv": "sensitive_access",
    "login_attempts.csv": "login_attempts",
    "threat_labels.csv": "threat_labels",
}


def ingest():
    logger.info("Starting data ingestion...")

    for filename, name in DATASETS.items():
        raw_file = PATHS["raw"] / filename
        target_file = PATHS["data"] / filename

        if not raw_file.exists():
            logger.warning(f"Missing raw file: {raw_file}")
            continue

        raw_df = pd.read_csv(raw_file)
        if target_file.exists():
            existing = pd.read_csv(target_file)
            combined = pd.concat([existing, raw_df], ignore_index=True)
            combined = combined.drop_duplicates()
        else:
            combined = raw_df

        combined.to_csv(target_file, index=False)
        logger.info(f"✅ Ingested {name}: {len(combined)} rows")


if __name__ == "__main__":
    ingest()
