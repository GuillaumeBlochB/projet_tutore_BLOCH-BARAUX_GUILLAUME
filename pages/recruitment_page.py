from locators.recruitment_locators import RecruitmentLocators
from .base_page import BasePage

import time 

class RecruitmentPage(BasePage):
    def open(self):
        super().open("/recruitment/viewCandidates")

    def get_options(self):
        """From an open list of options, retrieves the options"""
        return self.get_elements(RecruitmentLocators.DROPDOWN_OPTIONS)
    
    def select_option(self, value: str):
        """Selects a value from the dropdown

        Args:
            value (str): The option to select
        """
        options = self.get_options()

        for option in options:
            if value in option.text:
                option.click()
                return

        raise ValueError(f"Option '{value}' not found in dropdown")

    def get_dropdown_options(self, locator: tuple) -> list:
        """Opens the specified dropdown and retrieves its options

        Args:
            locator (tuple): 

        Returns:
            list: Returns a list of WebElements containing the options from the opened dropdown
        """        
        self.wait_for_element_visible(RecruitmentLocators.RESULTS_TABLE)
        time.sleep(1)
        self.click(locator)
        return self.get_options()
    
    def filter_results(self):
        """Clicks the search button to filter results"""        
        self.click(RecruitmentLocators.SEARCH_BTN)

    def filter_and_search(self, filters: dict):
        """Selects options for each dropdown and filters results

        Args:
            filters (dict): {locator: value}
        """
        self.wait_for_element_visible(RecruitmentLocators.RESULTS_TABLE)
        time.sleep(1)
        for locator, value in filters.items():
            self.click(locator)
            self.select_option(value)

        self.filter_results()
