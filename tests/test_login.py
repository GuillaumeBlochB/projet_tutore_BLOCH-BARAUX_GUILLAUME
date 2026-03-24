from utils.logger import logger
from pages.dashboard_page import DashboardPage
from pages.password_forgotten_page import PasswordForgottenPage
from config import settings

def test_login_success(login_page):
    """A test verifying proper login with correct credentials. Asserts URL of landing page and going to dashboard"""    
    
    logger.info("Verifying URL")
    assert login_page.is_loaded()

    logger.info("Entering credentials")
    login_page.login(settings.USERNAME, settings.PASSWORD)

    dashboard_page = DashboardPage(login_page.driver)
    
    logger.info("Verifying dashboard URL")
    dashboard_page.wait_for_url_contains("/dashboard")
    assert dashboard_page.is_loaded()

def test_login_failed(login_page):
    """A test verifying failed login with incorrect credentials. Asserts URL of landing page and proper display of error message"""    

    logger.info("Verifying URL")
    assert login_page.is_loaded()

    logger.info("Entering wrong credentials")
    login_page.login("BogusUsername", "BogusPassword")
    error_message = login_page.get_error_message()

    logger.info("Checking error message")
    assert error_message == "Invalid credentials"

def test_field_required(login_page):
    """A test verifying the proper display of required fields for missing inputs"""
    
    logger.info("Trying to log in without credentials")
    login_page.click_login()
    required_fields = login_page.get_required_fields()
    
    logger.info("Expecting 2 required fields")
    assert len(required_fields) == 2
    assert all(x.text == "Required" for x in required_fields)

def test_navigation_to_password_forgotten(login_page):
    """Clicks on the password forgotten link and asserts proper navigation"""    
    logger.info("Clicking on Forgot your password")
    login_page.click_forgot_password()

    password_forgotten_page = PasswordForgottenPage(login_page.driver)

    logger.info("Verifying password forgotten URL")
    password_forgotten_page.wait_for_url_contains("/requestPasswordResetCode")
    assert password_forgotten_page.is_loaded()