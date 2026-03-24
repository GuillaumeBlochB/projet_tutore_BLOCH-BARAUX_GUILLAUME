from .base_page import BasePage

class LoginPage(BasePage):
    def open(self):
        super().open("/web/index.php/auth/login")