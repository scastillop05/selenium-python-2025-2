from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResultsPage(BasePage):
    ARTIST_LINK = (By.CLASS_NAME, "link-block-target")

    def click_artist_link(self):
        self.click(self.ARTIST_LINK)