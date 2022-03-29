from ui.locators.basic_locators import UnauthorizedMainPageLocators, AuthorizedMainPageLocators
from ui.pages.base_page import BasePage


class AuthorizedMainPage(BasePage):
    def should_not_be_log_in_button(self):
        assert self.is_not_element_present(UnauthorizedMainPageLocators.LOG_IN_BUTTON), \
            "Log in button is presented, but should not be"

    def should_be_log_out_button(self):
        assert self.is_element_present(AuthorizedMainPageLocators.LOG_OUT_BUTTON), \
            "Log out is not presented, but should be"

    def log_out(self):
        self.click(AuthorizedMainPageLocators.RIGHT_MODULE_BUTTON)
        self.click(AuthorizedMainPageLocators.LOG_OUT_BUTTON)



