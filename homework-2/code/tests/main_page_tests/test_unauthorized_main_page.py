import pytest

from ui.pages.modal_panels.log_in_modal_panel import LogInModalPanel


@pytest.mark.UI
@pytest.mark.nologin
def test_log_in_with_incorrect_data(browser, unauthorized_main_page):
    page = unauthorized_main_page
    page.go_to_log_in_modal_panel_via_button()
    log_in_modal_panel = LogInModalPanel(browser, browser.current_url)
    log_in_modal_panel.failed_log_in("someEmail@a.ru", "somePassword")


@pytest.mark.UI
@pytest.mark.nologin
def test_log_in_without_required_fields(browser, unauthorized_main_page):
    page = unauthorized_main_page
    page.go_to_log_in_modal_panel_via_button()
    log_in_modal_panel = LogInModalPanel(browser, browser.current_url)
    log_in_modal_panel.failed_log_in("", "")

