from utils.logger import logger

def test_send_password(pw_forgotten_page):
    """A test verifying the confirmation of a link being sent to an email"""
      
    logger.info("Sending a reset link")
    pw_forgotten_page.reset_password("AnyUsername")
    
    logger.info("Checking if landing on reset successful")
    assert "/sendPasswordReset" in pw_forgotten_page.get_current_url()


