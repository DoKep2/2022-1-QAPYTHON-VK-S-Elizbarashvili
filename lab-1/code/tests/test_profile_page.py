import pytest

from ui.pages.log_in_modal_panel import LogInModalPanel
from ui.pages.profile_page import ProfilePage
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


def test_user_can_change_name(browser):
    link = "https://target.my.com/profile/contacts"
    page = ProfilePage(browser, link)
    page.open()
    page.change_full_name()


def test_user_can_change_phone_number(browser):
    link = "https://target.my.com/profile/contacts"
    page = ProfilePage(browser, link)
    page.open()
    page.change_phone_number()
