from .locators import RegPageLocators
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage():

    def __init__(self, url):
        self.browser = wd.Chrome()
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def close(self):
        self.browser.quit()

    def refresh(self):
        self.browser.refresh()

    def check_for_elements_presens(self):
        self.should_be_name_field()
        self.should_be_email_field()
        self.should_be_password_field()
        self.should_be_repeat_password_field()
        self.should_be_birthday_field()
        self.should_be_description_field()
        self.should_be_register_button()

    def enter_data(self, name, email, upass, rpass, birth, descr=''):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(upass)
        self.enter_repeat_password(rpass)
        self.enter_birthdate(birth)
        self.enter_description(descr)
        self.browser.find_element(*RegPageLocators.REG_BUTTON).click()

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((how, what)))
            self.browser.find_element(how, what)
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def should_be_name_field(self):
        assert self.is_element_present(*RegPageLocators.NAME_FIELD), 'Can\'t find "Name" field'

    def should_be_email_field(self):
        assert self.is_element_present(*RegPageLocators.EMAIL_FIELD), 'Can\'t find "Email" field'

    def should_be_password_field(self):
        assert self.is_element_present(*RegPageLocators.PASSWORD_FIELD), 'Can\'t find "Password" field'

    def should_be_repeat_password_field(self):
        assert self.is_element_present(*RegPageLocators.REPEAT_PASSWORD_FIELD), 'Can\'t find "Repeat password" field'

    def should_be_birthday_field(self):
        assert self.is_element_present(*RegPageLocators.BIRTHDAY_FIELD), 'Can\'t find "Birthday" field'

    def should_be_description_field(self):
        assert self.is_element_present(*RegPageLocators.DESCRIPTION_FIELD), 'Can\'t find "Description" field'

    def should_be_register_button(self):
        assert self.is_element_present(*RegPageLocators.REG_BUTTON), 'Can\'t find "Register" button'

    def enter_name(self, name):
        self.browser.find_element(*RegPageLocators.NAME_FIELD).send_keys(name)

    def enter_email(self, email):
        self.browser.find_element(*RegPageLocators.EMAIL_FIELD).send_keys(email)

    def enter_password(self, upass):
        self.browser.find_element(*RegPageLocators.PASSWORD_FIELD).send_keys(upass)

    def enter_repeat_password(self, rpass):
        self.browser.find_element(*RegPageLocators.REPEAT_PASSWORD_FIELD).send_keys(rpass)

    def enter_description(self, descr):
        self.browser.find_element(*RegPageLocators.DESCRIPTION_FIELD).send_keys(descr)

    def enter_birthdate(self, birth):
        self.browser.find_element(*RegPageLocators.BIRTHDAY_FIELD).send_keys(birth)

    def should_be_invalid_feedback(self):
        return self.is_element_present(*RegPageLocators.INVALID_FEEDBACK)

    def register_success(self, text='',):
        try:
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print (alert_text, text)
            return True
        except NoAlertPresentException:
            print('Register error')
            return False


