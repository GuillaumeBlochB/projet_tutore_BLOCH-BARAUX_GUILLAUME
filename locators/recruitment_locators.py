from selenium.webdriver.common.by import By

class RecruitmentLocators:
    JOB_TITLE_SELECT = (By.XPATH, "//label[text()='Job Title']/following::div[contains(@class,'oxd-select-text')][1]")
    STATUS_SELECT = (By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
    DROPDOWN_OPTIONS = (By.XPATH, "//div[@role='option']")
    SEARCH_BTN = (By.XPATH, "//form//button[@type='submit']")
    RESULTS_TABLE = (By.CLASS_NAME, "oxd-table-body")
    RESULTS_COUNT = (By.XPATH, "//span[contains(normalize-space(), 'Record Found')]")
    NO_RECORDS_TEXT = (By.XPATH, "//span[normalize-space()='No Records Found']")
    TOAST_MESSAGE = (By.XPATH, "//div[@id='oxd-toaster_1']//p[1]")