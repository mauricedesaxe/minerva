import logging
import sys
from pathlib import Path
from typing import Optional

from .config import get_config

def setup_logging(log_level: str = "INFO", log_file: Optional[Path] = None) -> None:
    """Setup basic logging configuration.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional path to log file. If None, logs only to console
    """
    # Create logs directory if logging to file
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Basic format that's easy to read
    log_format = "%(asctime)s | %(levelname)s | %(message)s"
    
    # Reset any existing handlers
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file, mode='w'))
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=handlers,
        force=True  # Force reconfiguration
    )

def get_logger(name: str) -> logging.Logger:
    """Get a logger with the given name."""
    logger = logging.getLogger(name)
    # Get the root logger's level
    root_level = logging.getLogger().getEffectiveLevel()
    # Set level on both logger and its handlers
    logger.setLevel(root_level)
    for handler in logger.handlers:
        handler.setLevel(root_level)
    return logger 