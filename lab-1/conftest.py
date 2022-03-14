import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome',
                     help='Choose necessary browser')
    parser.addoption("--language", action='store', default='en',
                     help='Choose necessary language')


@pytest.fixture
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {'intl.accept_languages': language})
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        pass
    yield browser
    time.sleep(3)
    browser.quit()
