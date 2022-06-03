import allure
import pytest

from conftest import MySql
from ui.data.enums.block_links_names import BlockLinksNames
from ui.data.enums.navbar_links_names import NavbarLinksNames
from ui.tests import LOGIN_PAGE_URL


class TestMainPage(MySql):
    """
        Корректный логаут через UI кнопку
        Шаги выполнения:
        - На главной нажать на кнопку логаута
        Ожидаемый результат:
        - Разлогинивание пользователя
        - Смена статуса в базе данных
        - Переход на страницу логина
    """

    @allure.epic('UI tests')
    @allure.title('User logout')
    def test_logout(self, main_page):
        current_user_username = self.client.get_current_user()[0].username
        main_page.logout()
        assert main_page.browser.current_url == LOGIN_PAGE_URL
        current_user = self.client.get_users_by_username(current_user_username)[0]
        assert current_user.active == 0

    """
        БАГ. Логаут для пользователя с длинной фамилией
        Шаги выполнения:
        - Залогиниться под пользователем с фамилией длиной в 255 символов
        Ожидаемый результат:
        - Разлогинивание пользователя
        - Смена статуса в базе данных
        - Переход на страницу логина
        Фактический результат:
        - Кнопка логаута пропадает, разлогинивание не происходит
    """

    @allure.epic('UI tests')
    @allure.title('User logout with too long surname')
    @pytest.mark.nologin
    @pytest.mark.xfail
    def test_logout_bug(self, register_page):
        data = register_page.fake_invalid_user_data(surname='a' * 255)
        main_page = register_page.register(data['name'],
                                           data['surname'],
                                           data['username'],
                                           data['email'],
                                           data['password'],
                                           data['password'],
                                           data['middle_name'])
        main_page.logout()
        assert main_page.browser.current_url == LOGIN_PAGE_URL

    """
        Переходы по ссылкам в навбаре
        Шаги выполнения:
        - Перейти по ссылкам в навбаре
        - Сравнить ожидаемые ссылки с фактическими
        Ожидаемый результат:
        - Ссылки совпадают
    """

    @allure.epic('UI tests')
    @allure.title('Go navbar links')
    @pytest.mark.parametrize("link_name", [
        NavbarLinksNames.PYTHON_HISTORY,
        NavbarLinksNames.FLASK,
        NavbarLinksNames.CENTOS,
        NavbarLinksNames.WIRESHARK_NEWS,
        NavbarLinksNames.WIRESHARK_DOWNLOAD,
        NavbarLinksNames.TCPDUMP_EXAMPLES])
    def test_go_navbar_link(self, main_page, link_name):
        main_page.go_navbar_link(link_name)
        main_page.navbar_link_transition_is_correct(link_name)

    """
        БАГ. Переходы по ссылкам в навбаре
        Шаги выполнения:
        - Залогиниться под пользователем с фамилией длиной в 255 символов
        - Кликнуть по кнопкам в навбаре
        Ожидаемый результат:
        - Открытие выпадающих списков / переход на соответствующую страницу
        Фактический результат:
        - Нарушение кликбокса кнопок навбара, открытие выпадающих списков /
         переход на соответствующую страницу не происходит
    """

    @allure.epic('UI tests')
    @allure.title('Go navbar link bug')
    @pytest.mark.nologin
    @pytest.mark.xfail
    @pytest.mark.parametrize("link_name", [
        NavbarLinksNames.PYTHON_HISTORY,
        NavbarLinksNames.FLASK,
        NavbarLinksNames.CENTOS,
        NavbarLinksNames.WIRESHARK_NEWS,
        NavbarLinksNames.WIRESHARK_DOWNLOAD,
        NavbarLinksNames.TCPDUMP_EXAMPLES])
    def test_go_navbar_link_bug(self, register_page, main_page, link_name):
        data = register_page.fake_invalid_user_data(surname='a' * 255)
        main_page = register_page.register(data['name'],
                                           data['surname'],
                                           data['username'],
                                           data['email'],
                                           data['password'],
                                           data['password'],
                                           data['middle_name'])
        main_page.go_navbar_link(link_name)
        main_page.navbar_link_transition_is_correct(link_name)

    """
        Переходы по ссылкам в блоках на главной
        Шаги выполнения:
        - Кликнуть по блокам по центру главной страницы
        Ожидаемый результат:
        - Переход на соответствующую страницу
    """

    @allure.epic('UI tests')
    @allure.title('Go content block links')
    @pytest.mark.parametrize("link_name", [
        BlockLinksNames.API,
        BlockLinksNames.INTERNET,
        BlockLinksNames.SMTP
    ])
    def test_go_content_block_links(self, main_page, link_name):
        main_page.go_to_content_block_page(link_name)
        main_page.block_link_transition_is_correct(link_name)
