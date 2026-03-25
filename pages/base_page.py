from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path=""):
        self.driver.get(BASE_URL + path)

    
    def wait_for_element_visible(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
    )

    def is_loaded(self, path:str) -> bool:
        """Checks if the requested path is present in URL

        Args:
            path (str): The path to check against the URL

        Returns:
            bool: Is the path in URL ?
        """        
        return path in self.get_current_url()

    def click(self, locator: tuple, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()
    
    def enter_text(self, locator, text, timeout=15):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator, timeout=15):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return elem.text

    def get_current_url(self):
        return self.driver.current_url


    def get_elements(self, locator, timeout=15):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return elem

    def wait_for_url_contains(self, partial_url, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )