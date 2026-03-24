from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//form//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[@role='alert']//p")
    REQUIRED_MESSAGE = (By.XPATH, "//span[contains(@class, 'oxd-input-field-error-message')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(@class, 'orangehrm-login-forgot-header')]")