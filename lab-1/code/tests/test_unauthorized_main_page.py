import pytest
from ui.pages.log_in_modal_panel import LogInModalPanel
from ui.pages.unauthorized_main_page import UnauthorizedMainPage


def test_guest_can_log_in(browser):
    LOGIN = "esmbot@yandex.ru"
    PASSWORD = "36hrzUCPJj-&T2."
    link = "https://target.my.com/"
    page = UnauthorizedMainPage(browser, link)
    page.open()
    page.go_to_log_in_modal_panel_via_button()
    log_in_modal_panel = LogInModalPanel(browser, link)
    log_in_modal_panel.log_in(LOGIN, PASSWORD)


def test_guest_should_see_log_in_button(browser):
    link = "https://target.my.com/dashboard"
    page = UnauthorizedMainPage(browser, link)
    page.open()
    page.should_be_log_in_button()