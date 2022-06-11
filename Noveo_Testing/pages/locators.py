from selenium.webdriver.common.by import By

class RegPageLocators():
        NAME_FIELD = (By.CSS_SELECTOR, '#name')
        EMAIL_FIELD = (By.CSS_SELECTOR, '#email')
        PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
        REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, '#repeat_password')
        BIRTHDAY_FIELD = (By.CSS_SELECTOR, '#birthday')
        DESCRIPTION_FIELD = (By.CSS_SELECTOR, '#description')
        REG_BUTTON = (By.CSS_SELECTOR, '.btn')
        INVALID_FEEDBACK = (By.CSS_SELECTOR, '.invalid-feedback')
