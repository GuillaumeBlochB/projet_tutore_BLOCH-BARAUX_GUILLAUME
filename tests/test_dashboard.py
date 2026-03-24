from utils.logger import logger
from collections import Counter

def test_check_dashboard_elements(dashboard_page):
    """Checks if all elements in the dashboard are present"""
    
    logger.info("Fetching elements")
    widget_names = dashboard_page.get_dashboard_elements()

    widget_elements = ["time at work", "my actions", "quick launch", "buzz latest posts", "employees on leave today", "employee distribution by sub unit", "employee distribution by location"]

    assert Counter(widget_names) == Counter(widget_elements)

def test_check_dashboard_side_panel_elements(dashboard_page):
    """Checks if all elements of the side panel are present"""

    logger.info("Retrieving side panel elements")
    side_panel_links = dashboard_page.get_dashboard_side_panel()

    logger.info("Checking if all links are present")
    logger.info(f"{len(side_panel_links)} elements retrieved")
    assert len(side_panel_links) == 12

    logger.info("Asserting names of links")
    link_names = ["admin", "pim", "leave", "time", "recruitment", "my info", "performance", "dashboard", "directory", "maintenance", "claim", "buzz"]

    assert Counter(link_names) == Counter(side_panel_links)

def test_filter_dashboard_side_panel_elements(dashboard_page):
    """Checks if the side panels filters properly"""

    logger.info("Filtering using Admin as a value")
    filtered_panel_links = dashboard_page.get_filtered_dashboard_side_panel("Admin")
    
    logger.info(f"{len(filtered_panel_links)} elements found after filtering")
    assert len(filtered_panel_links) == 1

    assert filtered_panel_links[0] == "admin"



