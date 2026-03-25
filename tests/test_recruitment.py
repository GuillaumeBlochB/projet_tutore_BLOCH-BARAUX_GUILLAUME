from utils.logger import logger
from locators.recruitment_locators import RecruitmentLocators

def test_get_options(recruitment_page):
    """A test to check if the options fetched in a dropdown are correct"""

    recruitment_page.open()

    logger.info("Verifying URL")
    assert recruitment_page.is_loaded("/recruitment/viewCandidates")

    logger.info("Selecting the status dropdown")
    options = [x.text for x in recruitment_page.get_dropdown_options(RecruitmentLocators.STATUS_SELECT)][1:] # We're not taking the -- Select -- option

    logger.info(f"{len(options)} options retrieved")
    assert len(options) == 9

def test_filter_option_results_found(recruitment_page):
    """Filtering the results by Job Title and Status and checking for presence of results"""

    recruitment_page.open()

    logger.info("Verifying URL")
    assert recruitment_page.is_loaded("/recruitment/viewCandidates")

    filters = {
        RecruitmentLocators.JOB_TITLE_SELECT: "Account Assistant",
        RecruitmentLocators.STATUS_SELECT: "Application Initiated"
    }

    logger.info("Selecting option in dropdowns")
    recruitment_page.filter_and_search(filters)

    logger.info("Fetching count of records found")
    results = recruitment_page.get_records_count()

    logger.info(f"Found {results} results")
    assert results == 1

def test_filter_option_no_results(recruitment_page):
    """Fitlering the results by Job Title and Status and checking for the absence of results and display of the Toaster"""  

    recruitment_page.open()

    logger.info("Verifying URL")
    assert recruitment_page.is_loaded("/recruitment/viewCandidates")

    filters = {
        RecruitmentLocators.JOB_TITLE_SELECT: "Account Assistant",
        RecruitmentLocators.STATUS_SELECT: "Interview Passed"
    }

    logger.info("Selecting option in dropdowns")
    recruitment_page.filter_and_search(filters)

    logger.info("Fetching count of records found")
    results = recruitment_page.get_records_count()

    logger.info(f"Found {results} results")
    assert results == 0

    logger.info("Checking for Info toaster")
    el = recruitment_page.get_toaster_text()
    assert el == "Info"
    