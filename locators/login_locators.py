from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//form//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[@role='alert']//p")