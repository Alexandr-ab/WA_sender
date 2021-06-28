from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
import time
import math

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=5):
        try:
            self.browser.implicitly_wait(timeout)
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_desapeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f'Your code: {alert.text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def go_to_the_basket(self):
        assert self.is_element_present(*BasePageLocators.GO_TO_THE_BASKET_BUTTON), 'Can\'t find cart button'
        self.browser.find_element(*BasePageLocators.GO_TO_THE_BASKET_BUTTON).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"