import pytest
from utils.driver_factory import get_driver
from config.settings import BASE_URL

DEBUG = True

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver

    if DEBUG:
        input("Press Enter to close the browser...")

    driver.quit()