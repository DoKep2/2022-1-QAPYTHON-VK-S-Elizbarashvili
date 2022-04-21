import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome',
                     help='Choose necessary browser')
    parser.addoption("--language", action='store', default='en',
                     help='Choose necessary language')
    parser.addoption("--selenoid", action="store_true")
    parser.addoption("--vnc", action="store_true")


@pytest.fixture(scope="session")
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope="function", autouse=True)
def log_in(browser, request):
    if 'nologin' in request.keywords:
        return
    LOGIN = "esmbot@yandex.ru"
    PASSWORD = "36hrzUCPJj-&T2."
    link = "https://target.my.com/"
    from ui.pages.basic_pages.unauthorized_main_page import UnauthorizedMainPage
    page = UnauthorizedMainPage(browser, link)
    page.open()
    browser.maximize_window()
    page.go_to_log_in_modal_panel_via_button()
    from ui.pages.modal_panels.log_in_modal_panel import LogInModalPanel
    log_in_modal_panel = LogInModalPanel(browser, link)
    log_in_modal_panel.successful_log_in(LOGIN, PASSWORD)
    from ui.pages.basic_pages.authorized_main_page import AuthorizedMainPage
    return AuthorizedMainPage(browser, browser.current_url)


@pytest.fixture
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    capabilities = {
        'browserName': 'chrome',
        'version': '98.0'
    }
    if request.config.getoption("--selenoid"):
        if request.config.getoption("--vnc"):
            capabilities['enableVNC'] = True
        browser = webdriver.Remote(
            'http://localhost:4444/wd/hub',
            options=Options(),
            desired_capabilities=capabilities
        )
    elif browser_name == "chrome":
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
    browser.quit()


@pytest.fixture(scope="function")
def unauthorized_main_page(browser):
    url = "https://target.my.com/"
    from ui.pages.basic_pages.unauthorized_main_page import UnauthorizedMainPage
    page = UnauthorizedMainPage(browser, url)
    page.open()
    return page


@pytest.fixture(scope="function")
def campaigns_page(browser):
    url = "https://target.my.com/dashboard/"
    from ui.pages.navbar_pages.campaigns_page import CampaignsPage
    page = CampaignsPage(browser, url)
    page.open()
    return page


@pytest.fixture(scope="function")
def audiences_page(browser):
    url = "https://target.my.com/segments/segments_list"
    from ui.pages.navbar_pages.audiences_page import AudiencesPage
    page = AudiencesPage(browser, url)
    page.open()
    return page

