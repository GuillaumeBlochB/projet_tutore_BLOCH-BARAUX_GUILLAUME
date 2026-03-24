from .base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def open(self):
        super().open("/web/index.php/auth/login")

    def enter_username(self, username: str | None):
        """Inputs a username in the username field

        Args:
            username (str | None): The username
        """        
        self.enter_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password: str | None):
        """Inputs a password in the password field

        Args:
            password (str | None): The password
        """        
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Clicks on the login button"""        
        self.click(LoginLocators.LOGIN_BUTTON)
    
    def login(self, username: str | None = None, password: str | None = None):
        """Inputs credentials and logs in

        Args:
            username (str | None): The username
            password (str | None): The password
        """        
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Retrieves the error message displayed on unsuccessful login"""        
        return self.get_text(LoginLocators.ERROR_MESSAGE)
    
    def get_required_fields(self):
        """Fetches all required fields of a form"""        
        return self.get_elements(LoginLocators.REQUIRED_MESSAGE)
    
    def click_forgot_password(self):
        """Navigates to the password forgotten page"""
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)