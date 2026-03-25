from selenium.webdriver.common.by import By

class RecruitmentLocators:
    JOB_TITLE_SELECT = (By.XPATH, "//label[text()='Job Title']/following::div[contains(@class,'oxd-select-text')][1]")
    STATUS_SELECT = (By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
    DROPDOWN_OPTIONS = (By.XPATH, "//div[@role='option']")
    SEARCH_BTN = (By.XPATH, "//form//button[@type='submit']")
    RESULTS_TABLE = (By.CLASS_NAME, "oxd-table-body")
