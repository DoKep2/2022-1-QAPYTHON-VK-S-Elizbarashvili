import pytest

from navbar_page_names import NavbarPageNames
from ui.pages.authorized_main_page import AuthorizedMainPage
from ui.pages.log_in_modal_panel import LogInModalPanel
from ui.pages.navbar_page import NavbarPage
from ui.pages.unauthorized_main_page import UnauthorizedMainPage


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    LOGIN = "esmbot@yandex.ru"
    PASSWORD = "36hrzUCPJj-&T2."
    link = "https://target.my.com/"
    page = UnauthorizedMainPage(browser, link)
    page.open()
    page.go_to_log_in_modal_panel_via_button()
    log_in_modal_panel = LogInModalPanel(browser, link)
    log_in_modal_panel.log_in(LOGIN, PASSWORD)


def test_user_can_log_out(browser):
    link = "https://target.my.com/dashboard"
    page = AuthorizedMainPage(browser, link)
    page.log_out()


@pytest.mark.parametrize('navbar_page_name',
                         [NavbarPageNames.CAMPAIGNS,
                          NavbarPageNames.AUDIENCES,
                          NavbarPageNames.BILLING,
                          NavbarPageNames.STATISTICS,
                          NavbarPageNames.PRO,
                          NavbarPageNames.PROFILE,
                          NavbarPageNames.TOOLS])
def test_user_can_switch_navbar_page(browser, navbar_page_name):
    link = "https://target.my.com/dashboard"
    page = NavbarPage(browser, link)
    page.open()
    browser.maximize_window()
    page.go_to_navbar_page(navbar_page_name)
    page.transition_is_correct(navbar_page_name)