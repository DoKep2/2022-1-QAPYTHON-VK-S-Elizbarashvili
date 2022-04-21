import pytest
from appium import webdriver

from ui import pages
from ui.capability import capability_select
from ui.pages.base_page import BasePage


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def login_page(driver, config):
    page = get_page('LoginPage')
    return page(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    page = get_page('MainPage')
    return page(driver=driver, config=config)


@pytest.fixture
def search_page(driver, config):
    page = get_page('SearchPage')
    return page(driver=driver, config=config)


@pytest.fixture
def title_page(driver, config):
    page = get_page('TitlePage')
    return page(driver=driver, config=config)


@pytest.fixture
def title_list_page(driver, config):
    page = get_page('TitleListPage')
    return page(driver=driver, config=config)


@pytest.fixture
def settings_page(driver, config):
    page = get_page('SettingsPage')
    return page(driver=driver, config=config)


@pytest.fixture
def news_source_page(driver, config):
    page = get_page('NewsSourcePage')
    return page(driver=driver, config=config)


@pytest.fixture
def about_page(driver, config):
    page = get_page('AboutPage')
    return page(driver=driver, config=config)


def get_page(page_class):
    page_class += 'ANDROID'
    page = getattr(pages, page_class, None)
    if page is None:
        raise Exception(f'No such page {page_class}')
    return page


def get_driver(appium_url, get_apk_name):
    desired_caps = capability_select(get_apk_name)
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    return driver


@pytest.fixture(scope='function')
def driver(config, get_apk_name):
    appium_url = config['appium']
    browser = get_driver(appium_url, get_apk_name)
    yield browser
    browser.quit()
