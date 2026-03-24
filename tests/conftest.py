import pytest
from utils.driver_factory import get_driver
from config.settings import BASE_URL
from pages.login_page import LoginPage
from pages.password_forgotten_page import PasswordForgottenPage

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

@pytest.fixture
def pw_forgotten_page(driver):
    page = PasswordForgottenPage(driver)
    page.open()
    return page