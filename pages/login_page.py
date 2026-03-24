from .base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def open(self):
        super().open("/web/index.php/auth/login")

    def enter_username(self, username):
        self.enter_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)
    
    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)