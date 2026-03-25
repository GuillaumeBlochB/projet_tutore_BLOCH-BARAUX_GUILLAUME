from .base_page import BasePage
from locators.password_forgotten_locators import PasswordForgottenLocators

class PasswordForgottenPage(BasePage):
    def open(self):
        super().open("/auth/requestPasswordResetCode")

    def enter_username(self, username: str):
        """Inputs a username in the username field

        Args:
            username (str): The username
        """        
        self.enter_text(PasswordForgottenLocators.USERNAME_INPUT, username)
   
    def click_reset_password(self):
        """Clicks on the Reset Password button"""
        self.click(PasswordForgottenLocators.RESET_PASSWORD_BUTTON)

    def reset_password(self, username: str):
        """Inputs username and presses reset password

        Args:
            username (str): The username
        """        
        self.enter_username(username)
        self.click_reset_password()        