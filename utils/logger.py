import logging
import os
from datetime import datetime

LOG_DIR = "logs"


def setup_logger():
    logger = logging.getLogger("ecommerce_test")

    if logger.handlers:
        return logger

    os.makedirs(LOG_DIR, exist_ok=True)

    log_file = f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(os.path.join(LOG_DIR, log_file), encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
