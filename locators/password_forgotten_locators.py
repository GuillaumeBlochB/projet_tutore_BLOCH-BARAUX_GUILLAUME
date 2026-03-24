from selenium.webdriver.common.by import By

class PasswordForgottenLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//form//button[@type='submit']")
