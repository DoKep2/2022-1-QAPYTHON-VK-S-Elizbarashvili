from ui.locators.basic_locators import LogInModalPanelLocators
from ui.pages.modal_panels.base_modal_panel import BaseModalPanel


class LogInModalPanel(BaseModalPanel):
    def successful_log_in(self, email, password):
        email_input = self.find(LogInModalPanelLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.find(LogInModalPanelLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit_button = self.find(LogInModalPanelLocators.SUBMIT_BUTTON)
        submit_button.click()
        authorized_page_url = "https://target.my.com/dashboard"
        assert self.browser.current_url == authorized_page_url

    def submit_button_is_disabled(self):
        submit_button = self.find(LogInModalPanelLocators.SUBMIT_BUTTON)
        disabled_btn_class_name = "authForm-module-disabled"
        return submit_button.get_attribute("class").__contains__(disabled_btn_class_name)

    def failed_log_in(self, email, password):
        email_input = self.find(LogInModalPanelLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.find(LogInModalPanelLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.submit_button_is_disabled()
        assert self.browser.current_url == "https://target.my.com/" or self.submit_button_is_disabled()
