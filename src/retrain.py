from logger import setup_logger
from main_execution import main

logger = setup_logger(__name__)


def retrain():
    logger.info("Scheduled retrain started")
    main()
    logger.info("Scheduled retrain complete")


if __name__ == "__main__":
    retrain()
