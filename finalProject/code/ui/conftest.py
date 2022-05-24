import os

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from config.creds import APP_PORT, APP_SERVICE
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.register_page import RegisterPage


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome',
                     help='Choose necessary browser')
    parser.addoption('--url', default=f'http://{APP_SERVICE}:{APP_PORT}')
    parser.addoption("--selenoid", action="store_true")
    parser.addoption("--vnc", action="store_true")


@pytest.fixture(scope="session")
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope="function", autouse=True)
def log_in(browser, request):
    if 'nologin' in request.keywords:
        return
    LOGIN = "DoKepDoKep"
    PASSWORD = "DoKepDoKep"
    link = f"http://{APP_SERVICE}:{APP_PORT}/login"
    page = LoginPage(browser, link)
    page.open()
    browser.maximize_window()
    page.login(LOGIN, PASSWORD)
    return MainPage(browser, browser.current_url)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser_name')
    return {'url': url, 'browser': browser}


def get_driver(config):
    browser_name = config['browser']
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.set_capability("browserVersion", "98.0")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        caps = {'browserName': browser_name,
                'version': '98.0'
                }
        browser = webdriver.Remote(command_executor=f"http://selenoid:4444/wd/hub",
                                   options=options, desired_capabilities=caps)
    else:
        raise KeyError
    return browser


@pytest.fixture(scope='function')
def browser(config):
    url = config['url']
    browser = get_driver(config)
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def login_page(browser):
    url = f"http://{APP_SERVICE}:{APP_PORT}/login"
    page = LoginPage(browser, url)
    page.open()
    browser.maximize_window()
    return page


@pytest.fixture(scope="function")
def main_page(browser):
    url = f"http://{APP_SERVICE}:{APP_PORT}/welcome/"
    page = MainPage(browser, url)
    page.open()
    browser.maximize_window()
    return page


@pytest.fixture(scope="function")
def register_page(browser):
    url = f"http://{APP_SERVICE}:{APP_PORT}/reg"
    page = RegisterPage(browser, url)
    page.open()
    browser.maximize_window()
    return page


