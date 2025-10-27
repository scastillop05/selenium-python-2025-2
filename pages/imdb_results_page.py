from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbResultsPage(BasePage):
    MOVIE_LINK = (By.CLASS_NAME, "ipc-metadata-list-summary-item__t")

    def click_movie_link(self):
        self.click(self.MOVIE_LINK)