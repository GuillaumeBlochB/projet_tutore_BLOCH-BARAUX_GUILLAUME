from .base_page import BasePage

class DashboardPage(BasePage):
    def is_loaded(self):
        return "dashboard" in self.get_current_url()
    
