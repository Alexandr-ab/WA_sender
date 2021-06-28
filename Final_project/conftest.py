import pytest
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     default='en', help='Choose language')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = wd.Chrome(options=options)
    yield browser
    # time.sleep(15000)
    browser.quit()