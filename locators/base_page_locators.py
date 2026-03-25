from selenium.webdriver.common.by import By

class BasePageLocators:
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown")
    LOGOUT_ITEM = (By.XPATH,  "//ul[contains(@class,'oxd-dropdown-menu')]//a[normalize-space()='Logout']")