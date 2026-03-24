from config.settings import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path=""):
        self.driver.get(BASE_URL + path)

    def click(self, locator: tuple):
        self.driver.find_element(*locator).click()
    
    def enter_text(self, locator: tuple, text: str):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.driver.find_element(*locator).text
