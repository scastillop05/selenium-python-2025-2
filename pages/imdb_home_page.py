from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbHomePage(BasePage):
    SEARCH_INPUT = (By.CLASS_NAME, "imdb-header-search__input")
    SEARCH_BTN = (By.CLASS_NAME, "ipc-icon--magnify")

    def search_movie(self, movie_name):
        self.click(self.SEARCH_INPUT)
        self.enter_text(self.SEARCH_INPUT, movie_name)
        self.click(self.SEARCH_BTN)