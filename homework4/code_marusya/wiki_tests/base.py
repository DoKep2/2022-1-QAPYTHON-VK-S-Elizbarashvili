import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages import MainPage, SettingsPage
from ui.pages.about_page import AboutPage
from ui.pages.base_page import BasePage
from ui.pages.request_permission_window import RequestPermissionWindow
from ui.pages.settings_element_pages import NewsSourcePage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger, ui_report):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.request_permission_window: RequestPermissionWindow = request.getfixturevalue('request_permission_window')
        self.settings_page: SettingsPage = request.getfixturevalue('settings_page')
        self.news_source_page: NewsSourcePage = request.getfixturevalue('news_source_page')
        self.about_page: AboutPage = request.getfixturevalue('about_page')

        self.request_permission_window.allow_request_permission()
        self.request_permission_window.allow_request_permission()
