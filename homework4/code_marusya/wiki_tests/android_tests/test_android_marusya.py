import pytest

from enums.news_source_names import NewsSourceNames
from wiki_tests.base import BaseCase


class TestWikipediaAndroid(BaseCase):

    @pytest.mark.AndroidUI
    def test_command_window_interaction(self):
        self.main_page.ask_Marusya("Russia", 'Россия')
        self.main_page.choose_question_from_suggest_carousel("население россии", "146 млн.")

    @pytest.mark.AndroidUI
    def test_calculator(self, math_expression = r"150 + 150"):
        self.main_page.compute_expression(math_expression)

    @pytest.mark.AndroidUI
    def test_mail_ru_news_source_activate(self):
        self.main_page.go_to_settings_page()
        self.settings_page.go_to_news_source_page()
        self.news_source_page.switch_news_source_status(NewsSourceNames.MAIL_RU)
        self.news_source_page.go_back_to_settings_page()
        self.settings_page.close_settings_page()
        self.main_page.ask_Marusya("News", "Включаю новости")

    @pytest.mark.AndroidUI
    def test_settings_interaction(self, repo_root):
        self.main_page.go_to_settings_page()
        self.settings_page.go_to_about_page()
        self.about_page.check_version(repo_root)

    @pytest.mark.AndroidUI
    def test_check_trademark(self):
        self.main_page.go_to_settings_page()
        self.settings_page.go_to_about_page()
        self.about_page.trademark_is_present()