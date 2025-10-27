from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbMoviePage(BasePage):
    MOVIE_TITLE = (By.CLASS_NAME, "hero__primary-text")

    def get_movie_title(self):
        return self.find_element(self.MOVIE_TITLE).text
    
    MOVIE_REVIEW = (By.CLASS_NAME, "sc-4dc495c1-1") 
    def get_movie_review(self):
        return self.find_element(self.MOVIE_REVIEW).text