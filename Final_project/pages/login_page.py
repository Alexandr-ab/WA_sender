from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'It\'s not a login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not presented'

    def register_new_user(self):
        email = str(time.time()) + '@neverbeen.com'
        password = 'fgehdikgnfht'
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
