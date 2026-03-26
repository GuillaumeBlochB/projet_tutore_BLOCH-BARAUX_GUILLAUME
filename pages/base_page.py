from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import BASE_URL, TIMEOUT
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path=""):
        self.driver.get(BASE_URL + path)

    
    def wait_for_element_visible(self, locator: tuple, timeout: int = TIMEOUT):
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

    def click(self, locator: tuple, timeout=TIMEOUT):
        """Clicks on the selected locator after waiting for it to be clickable

        Args:
            locator (tuple): The locator to click on
        """        
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()
    
    def enter_text(self, locator: tuple, text: str, timeout=TIMEOUT):
        """Clears and inputs given text into locator after waiting for it to be visible

        Args:
            locator (tuple): The locator to insert text into
            text (str): The text to write
        """        
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator: tuple, timeout=TIMEOUT) -> str:
        """Retrieves the text of a locator

        Args:
            locator (tuple): The locator to get the text from
        Returns:
            str: The locator's text
        """        
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return elem.text

    def get_current_url(self) -> str:
        """Retrieves the current URL

        Returns:
            str: The URL
        """        
        return self.driver.current_url

    def get_element(self, locator: tuple, timeout=TIMEOUT):
        """Get the first element matching the locator

        Args:
            locator (tuple): The locator
        """        
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return elem

    def get_elements(self, locator: tuple, timeout=TIMEOUT) -> list:
        """Get all elements matching the locator

        Args:
            locator (tuple): The locator
        Returns:
            list: Every WebElement items matching the locator
        """        
        elem = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return elem

    def wait_for_url_contains(self, partial_url: str, timeout=TIMEOUT):
        """Waits for the url to contain a string

        Args:
            partial_url (str): Part of or the whole URL
        """        
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )
    
    def logout(self):
        """Logs the user out by clicking on the dropdown and selecting Logout"""        
        self.click(BasePageLocators.USER_DROPDOWN)
        self.click(BasePageLocators.LOGOUT_ITEM)