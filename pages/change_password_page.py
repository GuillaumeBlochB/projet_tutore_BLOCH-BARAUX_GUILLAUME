from locators.change_password_locators import ChangePasswordLocators
from .base_page import BasePage

class ChangePasswordPage(BasePage):
    def open(self):
        super().open("/pim/updatePassword")

    def enter_current_password(self, password: str):
        """Enters the current password in the form

        Args:
            password (str): The current password
        """
        self.enter_text(ChangePasswordLocators.OLD_PASSWORD_INPUT, password)
    
    def enter_new_password(self, password: str):
        """Enters a new password in the form

        Args:
            password (str): The new password
        """        
        self.enter_text(ChangePasswordLocators.NEW_PASSWORD_INPUT, password)

    def enter_confirm_password(self, password: str):
        """Enters a password in the Confirm Password input

        Args:
            password (str): The confirmation password
        """        
        self.enter_text(ChangePasswordLocators.CONFIRM_PASSWORD_INPUT, password)

    def change_password(self):
        """Validates the change password form"""
        self.click(ChangePasswordLocators.SUBMIT_BTN)

    def fill_form(self, old_pw: str, new_pw: str, confirm_pw: str):
        """Fills and sends the form

        Args:
            old_pw (str): The old password
            new_pw (str): The new password
            confirm_pw (str): The confirmation of new password
        """        
        self.enter_current_password(old_pw)
        self.enter_new_password(new_pw)
        self.enter_confirm_password(confirm_pw)
        self.change_password()

    def get_toaster_text(self) -> str | bool:
        """Gets the value of the text present in the toaster if the toaster shows up

        Returns:
            str | bool: The toaster message if present
        """
        try:
            msg = self.get_element(ChangePasswordLocators.TOAST_MESSAGE).text
            return msg
        except:
            return False