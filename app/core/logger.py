import logging
import os
from logging.handlers import RotatingFileHandler
from app.core.config import settings

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def setup_logger():
    # Create logger with app name
    logger = logging.getLogger('mobile_factory')
    logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
    logger.propagate = False
    
    # Clear any existing handlers
    if logger.handlers:
        logger.handlers.clear()
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Info log handler
    info_handler = RotatingFileHandler(
        filename=os.path.join(LOG_DIR, 'info.log'),
        maxBytes=10485760,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    info_handler.setFormatter(formatter)
    info_handler.setLevel(logging.INFO)
    logger.addHandler(info_handler)
    
    # Error log handler
    error_handler = RotatingFileHandler(
        filename=os.path.join(LOG_DIR, 'error.log'),
        maxBytes=10485760,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    error_handler.setFormatter(formatter)
    error_handler.setLevel(logging.ERROR)
    logger.addHandler(error_handler)
    
    return logger

logger = setup_logger() 