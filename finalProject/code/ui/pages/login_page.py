from ui.locators.login_page_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.register_page import RegisterPage


class LoginPage(BasePage):
    def login(self, username, password):
        self.find(LoginPageLocators.USERNAME_INPUT).send_keys(username)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.find(LoginPageLocators.LOGIN_BUTTON).click()

    def go_to_register_page(self):
        link = self.find(LoginPageLocators.CREATE_ACCOUNT_LINK)
        link.click()
        return RegisterPage(self.browser, self.browser.current_url)

    def incorrect_username_or_password_alert_is_present(self):
        self.is_element_present(LoginPageLocators.INCORRECT_USERNAME_OR_PASSWORD_ALERT)

    def incorrect_username_length_alert_is_present(self):
        self.is_element_present(LoginPageLocators.INCORRECT_USERNAME_LENGTH_ALERT)
