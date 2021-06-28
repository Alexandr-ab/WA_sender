from selenium.webdriver.common.by import By

class BasePageLocators():
        LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
        LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
        GO_TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, 'span.btn-group a')
        USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
        LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
        REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
        REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
        REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
        REPEAT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
        REGISTER_BUTTON = (By.NAME, 'registration_submit')

class MainPageLocators():
        pass
        # def __init__(self, *args, **kwargs):
        #     super(MainPage, self).__init__(*args, **kwargs)

class ProductPageLocators():
        ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
        ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner strong')
        ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner :first-child strong')
        WATCHING_PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
        WATCHING_PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
        SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')

