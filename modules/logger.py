import logging
import sys
from typing import Optional

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'

class ColoredFormatter(logging.Formatter):
    """Custom formatter with colors"""
    
    format_str = "%(asctime)s - %(levelname)s - %(prefix)s%(message)s"
    
    FORMATS = {
        logging.DEBUG: Colors.HEADER + format_str + Colors.RESET,
        logging.INFO: Colors.INFO + format_str + Colors.RESET,
        logging.WARNING: Colors.WARNING + format_str + Colors.RESET,
        logging.ERROR: Colors.ERROR + format_str + Colors.RESET,
        logging.CRITICAL: Colors.ERROR + Colors.BOLD + format_str + Colors.RESET
    }

    def format(self, record):
        # Add prefix based on log type
        if not hasattr(record, 'prefix'):
            if 'embedding' in record.msg.lower():
                record.prefix = Colors.CYAN + "[EMBED] " + Colors.RESET
            elif any(x in record.msg.lower() for x in ['collection', 'chunk', 'document']):
                record.prefix = Colors.MAGENTA + "[STORE] " + Colors.RESET
            elif 'search' in record.msg.lower():
                record.prefix = Colors.SUCCESS + "[SEARCH] " + Colors.RESET
            else:
                record.prefix = ""
        
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def setup_logger(name: str = "minerva", level: Optional[int] = None) -> logging.Logger:
    """Set up a logger with colored output.
    
    Args:
        name: Logger name (default: "minerva")
        level: Logging level (default: INFO)
        
    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(name)
    
    # Set level (default to INFO if not specified)
    logger.setLevel(level or logging.INFO)
    
    # Create console handler with colored formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(ColoredFormatter())
    
    # Remove any existing handlers and add our console handler
    logger.handlers = []
    logger.addHandler(console_handler)
    
    return logger

# Create default logger instance
logger = setup_logger() 