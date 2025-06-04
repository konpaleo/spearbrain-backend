import logging

from app.core.settings import application_settings

logger = logging.getLogger("wtoc")
logger.propagate = False

if not logger.handlers:  # Add handlers only if none exist
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s: %(message)s", datefmt="%Y-%m-%dT%H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.setLevel(application_settings.LOGGER_LEVEL)
