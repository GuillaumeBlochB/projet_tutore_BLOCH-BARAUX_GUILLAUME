from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config import settings

def test_login_success(driver):
    """A test verifying proper login with correct credentials. Asserts URL of landing page and going to dashboard"""    
    login_page = LoginPage(driver)
    login_page.open()

    assert "/auth/login" in login_page.get_current_url()

    login_page.login(settings.USERNAME, settings.PASSWORD)

    dashboard_page = DashboardPage(driver)
    dashboard_page.wait_for_url_contains("/dashboard")
    assert dashboard_page.is_loaded()

def test_login_failed(driver):
    """A test verifying failed login with incorrect credentials. Asserts URL of landing page and proper display of error message"""    
    login_page = LoginPage(driver)
    login_page.open()

    assert "/auth/login" in login_page.get_current_url()

    login_page.login("BogusUsername", "BogusPassword")
    error_message = login_page.get_error_message()

    assert error_message == "Invalid credentials"