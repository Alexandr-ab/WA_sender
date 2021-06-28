from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_be_empty(self):
        self.go_to_the_basket()
        self.should_not_be_items()
        self.should_be_text_about_empty_basket()

    def should_not_be_items(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, '.basket-items'), 'Elements are presented, but should not be'

    def should_be_text_about_empty_basket(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#content_inner p').text.strip() == 'Your basket is empty. Continue shopping', 'The cart is not empty'