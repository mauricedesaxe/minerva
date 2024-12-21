import logging
import tempfile
from pathlib import Path
import time

import pytest

from minerva.logging import setup_logging, get_logger

def test_setup_logging_console():
    setup_logging()
    logger = get_logger("test")
    assert logger.level == logging.INFO

def test_setup_logging_file():
    with tempfile.TemporaryDirectory() as tmp_dir:
        log_file = Path(tmp_dir) / "test.log"
        setup_logging(log_level="DEBUG", log_file=log_file)
        logger = get_logger("test")

        # Test logging
        test_message = "Test log message"
        logger.info(test_message)
        
        # Give a small delay to ensure file writing is complete
        time.sleep(0.1)

        # Verify message was written to file
        assert log_file.exists()
        log_content = log_file.read_text()
        assert test_message in log_content

def test_get_logger():
    setup_logging(log_level="DEBUG")
    logger = get_logger("test")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test"

def test_logging_levels():
    with tempfile.TemporaryDirectory() as tmp_dir:
        log_file = Path(tmp_dir) / "test.log"
        setup_logging(log_level="INFO", log_file=log_file)
        # Get logger AFTER setting up logging with INFO level
        logger = get_logger("test")
        
        # These shouldn't appear (below INFO level)
        logger.debug("Debug message")
        
        # These should appear
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        
        # Force flush
        for handler in logger.handlers:
            handler.flush()
            
        content = log_file.read_text()
        assert "Debug message" not in content
        assert "Info message" in content
        assert "Warning message" in content
        assert "Error message" in content