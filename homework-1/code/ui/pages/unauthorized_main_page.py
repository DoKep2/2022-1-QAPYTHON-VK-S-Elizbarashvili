from ui.locators.basic_locators import UnauthorizedMainPageLocators
from ui.pages.base_page import BasePage


class UnauthorizedMainPage(BasePage):
    def go_to_log_in_modal_panel_via_button(self):
        log_in_btn = self.find(UnauthorizedMainPageLocators.LOG_IN_BUTTON)
        log_in_btn.click()

    def should_be_log_in_button(self):
        assert self.is_element_present(UnauthorizedMainPageLocators.LOG_IN_BUTTON), \
            "Log in button is not presented, but should be"
