import allure
import pytest

from conftest import MySql
from data_generator import MyFaker
from ui.locators.register_page_locators import RegisterPageLocators
from ui.tests import LOGIN_PAGE_URL, MAIN_PAGE_URL, REGISTER_PAGE_URL

faker = MyFaker()


class TestUI(MySql):
    """
        Переход на страницу логина
        Шаги воспроизведения:
        - Кликнуть на ссылку для перехода  на страницу логина
        Ожидаемый результат:
        - Переход на страницу логина
    """

    @allure.epic('UI tests')
    @allure.title('Go to login page')
    @pytest.mark.nologin
    def test_go_to_login_page(self, register_page):
        register_page.go_to_login_page()
        assert register_page.browser.current_url == LOGIN_PAGE_URL
    """
        *Примечание
        Все тесты кроме перехода на страницу логина помечены XFail, потому что в базу данных некорректно передаётся
        middle name, из-за чего тесты падают на проверке соответствующих данных пользователя
    """

    """
        Успешная регистрация пользователя
        Шаги воспроизведения:
        - Заполнить поля корректными данными, зарегистрироваться
        Ожидаемый результат:
        - Произошёл переход на главную
        - Пользователь добавился в базу данных
        - Пользователь добавился с соответствующими данными        
    """

    @allure.epic('UI tests')
    @allure.title('Valid register')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_valid_register(self, register_page):
        data = register_page.fake_invalid_user_data()
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            data['name'],
            data['surname'],
            data['username'],
            data['email'],
            data['password'],
            data['password'],
            data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert register_page.browser.current_url == MAIN_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 == users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too short name, BUG')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_register_with_too_short_name_bug(self, register_page):
        data = register_page.fake_invalid_user_data(name=faker.fake_too_short_name())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert 'Минимально допустимое количество символов: 6.' in register_page.find(RegisterPageLocators.NAME_INPUT) \
            .get_attribute('validationMessage')
        assert register_page.browser.current_url == REGISTER_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 != users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too long name')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_register_with_too_long_name(self, register_page):
        data = register_page.fake_invalid_user_data(name=faker.fake_too_long_name())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert register_page.browser.current_url == MAIN_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 == users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too short surname, BUG')
    @pytest.mark.nologin
    @pytest.mark.xfail
    def test_register_with_too_short_surname_bug(self, register_page):
        data = register_page.fake_invalid_user_data(surname=faker.fake_too_short_name())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert 'Минимально допустимое количество символов: 6.' in register_page.find(RegisterPageLocators.SURNAME_INPUT) \
            .get_attribute('validationMessage')
        assert register_page.browser.current_url == REGISTER_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 != users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with long surname, BUG')
    @pytest.mark.nologin
    @pytest.mark.xfail
    def test_register_with_too_long_surname_bug(self, register_page):
        data = register_page.fake_invalid_user_data(surname=faker.fake_too_long_name())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert register_page.browser.current_url == MAIN_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 == users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too long middlename, BUG')
    @pytest.mark.nologin
    @pytest.mark.xfail
    def test_register_with_too_long_middle_name_bug(self, register_page):
        data = register_page.fake_invalid_user_data(middle_name=MyFaker.fake_too_long_name())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert register_page.browser.current_url == MAIN_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 == users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too short username')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_register_with_too_short_username(self, register_page):
        data = register_page.fake_invalid_user_data(username=faker.fake_too_short_username())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert 'Минимально допустимое количество символов: 6.' in register_page.find(
            RegisterPageLocators.USERNAME_INPUT) \
            .get_attribute('validationMessage')
        assert register_page.browser.current_url == REGISTER_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 != users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too long username')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_register_with_too_long_username(self, register_page):
        data = register_page.fake_invalid_user_data(username=faker.fake_too_long_username())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert register_page.browser.current_url == MAIN_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 == users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too short email')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_register_with_too_short_email(self, register_page):
        data = register_page.fake_invalid_user_data(email=faker.fake_too_short_email())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert 'Минимально допустимое количество символов: 6.' in register_page.find(RegisterPageLocators.EMAIL_INPUT) \
            .get_attribute('validationMessage')
        assert register_page.browser.current_url == REGISTER_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 != users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with empty email, BUG')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_register_with_empty_email_bug(self, register_page):
        data = register_page.fake_invalid_user_data(email="")
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert 'Минимально допустимое количество символов: 6.' in register_page.find(RegisterPageLocators.EMAIL_INPUT) \
            .get_attribute('validationMessage')
        assert register_page.browser.current_url == REGISTER_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 != users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)

    @allure.epic('UI tests')
    @allure.title('Register with too long email')
    @pytest.mark.xfail
    @pytest.mark.nologin
    def test_register_with_too_long_email(self, register_page):
        data = register_page.fake_invalid_user_data(email=faker.fake_too_long_email())
        username = data['username'][:16]
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        register_page.register(
            name=data['name'],
            surname=data['surname'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            confirm_password=data['password'],
            middle_name=data['middle_name'])
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert register_page.browser.current_url == MAIN_PAGE_URL
        assert users_count_with_correspondent_name_before + 1 == users_count_with_correspondent_name_after
        assert self.client.user_was_created_with_correspondent_data(username, data)
