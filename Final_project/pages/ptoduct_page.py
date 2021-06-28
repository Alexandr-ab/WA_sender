from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_imet_to_the_basket(self):
        self.should_be_add_to_basket_button()
        self.add_to_basket()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Can\'t find \'Add to cart\' button'

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def checking_names_and_prices(self):
        self.should_be_the_name_of_the_added_product()
        self.should_be_the_price_of_the_added_product()
        self.check_the_name_of_the_added_product()
        self.check_the_price_of_the_added_product()
        self.should_be_the_success_message()

    def should_be_the_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Can\'t find the succses messages'

    def should_be_the_name_of_the_added_product(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), 'Can\'t find the added product name'
        self.added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

    def should_be_the_price_of_the_added_product(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_PRICE), 'Can\'t find the added product price'
        self.added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text

    def check_the_name_of_the_added_product(self):
        watching_product_name = self.browser.find_element(*ProductPageLocators.WATCHING_PRODUCT_NAME).text
        assert self.added_product_name == watching_product_name, 'The name of the added product is different than the name of the watching product'

    def check_the_price_of_the_added_product(self):
        watching_product_price = self.browser.find_element(*ProductPageLocators.WATCHING_PRODUCT_PRICE).text
        assert self.added_product_price == watching_product_price, 'The price of the added product is different than the price of the watching product'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def success_message_should_desapear(self):
        assert self.is_desapeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message should desapear, but it\'s still presented'



