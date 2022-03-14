from ui.locators.basic_locators import LogInModalPanelLocators
from ui.pages.base_modal_panel import BaseModalPanel


class LogInModalPanel(BaseModalPanel):
    def log_in(self, email, password):
        email_input = self.find(LogInModalPanelLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.find(LogInModalPanelLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit_button = self.find(LogInModalPanelLocators.SUBMIT_BUTTON)
        submit_button.click()
