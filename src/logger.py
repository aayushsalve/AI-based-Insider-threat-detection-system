import logging
from config import PATHS, LOGGING_CONFIG


def setup_logger(name):
    """Setup logging for modules"""
    logger = logging.getLogger(name)

    # Prevent duplicate handlers on repeated imports
    if logger.handlers:
        return logger

    logger.setLevel(LOGGING_CONFIG.get('level', 'INFO'))
    logger.propagate = False

    PATHS['logs'].mkdir(exist_ok=True)

    fh = logging.FileHandler(PATHS['logs'] / f'{name}.log', encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        LOGGING_CONFIG.get(
            'format',
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
