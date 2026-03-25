from .base_page import BasePage
from locators.dashboard_locators import DashboardLocators

class DashboardPage(BasePage):   
    def get_dashboard_elements(self) -> list:
        """Retrieves the name of all widgets present on the dashboard

        Returns:
            list: A list of all widget names found on the dashboard
        """        
        elems = self.get_elements(DashboardLocators.WIDGET_NAME)
        return [x.text.lower() for x in elems]
    
    def get_dashboard_side_panel(self) -> list[str]:
        """Retrieves the list of link names from the side panel

        Returns:
            list: A list of all link names
        """        
        elems = self.get_elements(DashboardLocators.SIDE_PANEL_LIST)
        return [elem.text.lower() for elem in elems]

    def get_filtered_dashboard_side_panel(self, text):
        """Filters the side panel elements by text input value"""
        self.enter_text(DashboardLocators.SEARCH_INPUT, text)
        return self.get_dashboard_side_panel()
