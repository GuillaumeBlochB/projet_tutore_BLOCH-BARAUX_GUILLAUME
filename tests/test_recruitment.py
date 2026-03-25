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
    