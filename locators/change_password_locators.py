from selenium.webdriver.common.by import By

class ChangePasswordLocators:
    OLD_PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Current Password']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    NEW_PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Password']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    SUBMIT_BTN = (By.XPATH, "//form//button[@type='submit']")
    TOAST_MESSAGE = (By.XPATH, "//div[@id='oxd-toaster_1']//p[1]")