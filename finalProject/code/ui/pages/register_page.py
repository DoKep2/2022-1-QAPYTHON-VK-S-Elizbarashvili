import ui.pages.login_page as login_page
import ui.pages.main_page as main_page
from data_generator import MyFaker
from ui.locators.register_page_locators import RegisterPageLocators
from ui.pages.base_page import BasePage

faker = MyFaker()


class RegisterPage(BasePage):
    def go_to_login_page(self):
        self.find(RegisterPageLocators.LOGIN_LINK).click()
        return login_page.LoginPage(self.browser, self.browser.current_url)

    def register(self, name, surname, username, email, password, confirm_password, middle_name):
        self.find(RegisterPageLocators.NAME_INPUT).send_keys(name)
        self.find(RegisterPageLocators.SURNAME_INPUT).send_keys(surname)
        self.find(RegisterPageLocators.MIDDLE_NAME_INPUT).send_keys(middle_name)
        self.find(RegisterPageLocators.USERNAME_INPUT).send_keys(username)
        self.find(RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        self.find(RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        self.find(RegisterPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)
        self.find(RegisterPageLocators.CONFIRM_CHECKBOX).click()
        self.find(RegisterPageLocators.SUBMIT_BUTTON).click()
        return main_page.MainPage(self.browser, self.browser.current_url)

    def fake_invalid_user_data(self,
                               name=None,
                               surname=None,
                               middle_name=None,
                               username=None,
                               password=None,
                               email=None,
                               confirm_password=None) -> dict:
        if name is None:
            name = faker.fake_valid_name()
        if surname is None:
            surname = faker.fake_valid_name()
        if middle_name is None:
            middle_name = faker.fake_valid_name()
        if username is None:
            username = faker.fake_valid_username()
        if password is None:
            password = faker.fake_valid_name()
        if email is None:
            email = faker.fake_valid_email()

        return {
            "name": name,
            "surname": surname,
            "middle_name": middle_name,
            "username": username,
            "password": password,
            "email": email,
            'confirm_password': password if confirm_password is None else confirm_password
        }
