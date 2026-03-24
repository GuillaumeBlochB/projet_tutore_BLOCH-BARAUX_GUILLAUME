import pytest
from utils.driver_factory import get_driver
from config.settings import BASE_URL
from pages.login_page import LoginPage

DEBUG = False

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver

    if DEBUG:
        input("Press Enter to close the browser...")

    driver.quit()

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page