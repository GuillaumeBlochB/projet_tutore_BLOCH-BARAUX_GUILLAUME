from utils.logger import logger
from config import settings
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

NEW_PASSWORD = "ASuperNewPassword123"

def test_change_password_success(change_password_page):
    """A test verifying a successful password change : the old password is inserted correctly, the new password matches requirements and confirm password matches"""

    change_password_page.open()

    logger.info("Verifying URL")
    assert change_password_page.is_loaded("/pim/updatePassword")

    logger.info("Inputing credentials")
    change_password_page.fill_form(settings.PASSWORD, NEW_PASSWORD, NEW_PASSWORD)

    logger.info("Checking for toaster showing up")
    el = change_password_page.get_toaster_text()
    assert el == "Success"

def test_change_password_current_password_incorrect(change_password_page):
    """A test verifying the toaster on an incorrect current password"""

    change_password_page.open()

    logger.info("Verifying URL")
    assert change_password_page.is_loaded("/pim/updatePassword")

    logger.info("Inputing credentials")
    change_password_page.fill_form(NEW_PASSWORD, NEW_PASSWORD, NEW_PASSWORD)

    logger.info("Checking for toaster showing up")
    el = change_password_page.get_toaster_text()
    assert el == "Error"

def test_change_password_and_log_in(change_password_page):
    """Changes password and then tries to reconnect using the new password"""

    change_password_page.open()

    logger.info("Verifying URL")
    assert change_password_page.is_loaded("/pim/updatePassword")

    logger.info("Inputing credentials")
    change_password_page.fill_form(settings.PASSWORD, NEW_PASSWORD, NEW_PASSWORD)

    logger.info("Checking for toaster showing up")
    el = change_password_page.get_toaster_text()
    assert el == "Success" 

    logger.info("Logging Out")
    change_password_page.logout()

    login_page = LoginPage(change_password_page.driver)

    logger.info("verifying URL of landing page")
    assert login_page.is_loaded("/auth/login")

    logger.info("Logging in with new password")
    login_page.login(settings.USERNAME, NEW_PASSWORD)

    dashboard_page = DashboardPage(login_page.driver)

    logger.info("Verifying proper landing on Dashboard")
    assert dashboard_page.is_loaded("/dashboard")



