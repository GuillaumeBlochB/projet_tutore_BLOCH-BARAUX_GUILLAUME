from selenium.webdriver.common.by import By

class DashboardLocators:
    WIDGET_NAME = (By.XPATH, "//div[contains(@class,'orangehrm-dashboard-widget-name')]//p[contains(@class, 'oxd-text--p')]")
    SIDE_PANEL_LIST = (By.XPATH, "//ul[@class='oxd-main-menu']//a")
    SEARCH_INPUT = (By.XPATH, "//div[contains(@class, '--fixed')]//input")