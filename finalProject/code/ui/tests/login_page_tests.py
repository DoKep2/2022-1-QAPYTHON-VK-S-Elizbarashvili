import allure
import pytest

from conftest import MySql
from ui.locators.login_page_locators import LoginPageLocators
from ui.tests import MAIN_PAGE_URL, LOGIN_PAGE_URL, REGISTER_PAGE_URL


class TestsLoginPage(MySql):

    """
        Корректный логин
        Шаги воспроизведения:
        - Залогиниться под существующим пользователем
        Ожидаемый результат:
        - Переход на главную страницу
    """

    @allure.epic('UI tests')
    @allure.title('User correct login')
    @pytest.mark.nologin
    def test_login(self, login_page):
        login_page.login("DoKepDoKep", "DoKepDoKep")
        assert login_page.browser.current_url == MAIN_PAGE_URL
        user = self.client.get_users_by_username("DoKepDoKep")[0]
        assert user.active == 1

    """
        Некорректный логин
        Шаги воспроизведения:
        - Залогиниться под несуществующим пользователем
        Ожидаемый результат:
        - Переход на главную страницу не происходит
    """

    @allure.epic('UI tests')
    @allure.title('User invalid login')
    @pytest.mark.nologin
    @pytest.mark.parametrize('username, password', [("invalidUsername", "invalidPassword")])
    def test_invalid_login(self, login_page, username, password):
        login_page.login(username, password)
        assert login_page.browser.current_url == LOGIN_PAGE_URL

    """
        Появление алерта о коротком имени пользователя
        Шаги воспроизведения:
        - Ввести имя пользователя длиной до 5 символов включитель
        Ожидаемый результат:
        - Алерт о коротком имени
    """

    @allure.epic('UI tests')
    @allure.title('User logn with too short username')
    @pytest.mark.nologin
    def test_login_with_too_short_username(self, login_page):
        login_page.login("aaa", "pass")
        assert 'Минимально допустимое количество символов: 6.' in login_page.find(LoginPageLocators.USERNAME_INPUT) \
            .get_attribute('validationMessage')



