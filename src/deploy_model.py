import logging
import shutil
from config import PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def deploy_model():
    """Deploy trained models to production"""
    logger.info("="*60)
    logger.info("DEPLOYING MODELS TO PRODUCTION")
    logger.info("="*60)
    
    models_dir = PATHS["models"]
    prod_dir = PATHS["data"] / "production_models"
    prod_dir.mkdir(exist_ok=True)
    
    # Copy all models
    for model_file in models_dir.glob("*.pkl"):
        dest = prod_dir / model_file.name
        shutil.copy(model_file, dest)
        logger.info(f"✅ Deployed: {model_file.name}")
    
    logger.info(f"\n✅ Models deployed to: {prod_dir}")
    logger.info("="*60)


if __name__ == "__main__":
    deploy_model()