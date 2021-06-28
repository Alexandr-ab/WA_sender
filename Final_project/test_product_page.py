import pytest
from .pages.ptoduct_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.need_review
# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# def test_guest_can_add_product_to_basket(browser, link):
def test_guest_can_add_product_to_basket(browser):
    # link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
    link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link2)
    page.open()
    page.add_imet_to_the_basket()
    page.solve_quiz_and_get_code()
    page.checking_names_and_prices()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_imet_to_the_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.is_desapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.should_be_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link2 = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link2)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_imet_to_the_basket()
        page.checking_names_and_prices()