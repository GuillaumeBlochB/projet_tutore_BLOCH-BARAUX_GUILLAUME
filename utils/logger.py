import logging
import os

LOG_FILE = os.path.join(os.getcwd(), "selenium_test.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, mode='w'),  # overwrite each run
        logging.StreamHandler()
    ]
)

logging.getLogger("selenium").setLevel(logging.INFO)
logger = logging.getLogger("selenium_logger")