from selenium.common.exceptions import TimeoutException

from enums.news_source_names import NewsSourceNames
from matchings.news_source_locator_matching import NewsSourceLocatorMatching
from ui.locators.locators_android import NewsSourcePageLocators
from ui.pages import BasePage


class SettingsElementPage(BasePage):
    pass


class NewsSourcePage(SettingsElementPage):
    def get_news_source_by_name(self, news_source_name: NewsSourceNames):
        pass

    @staticmethod
    def get_news_source_locator_by_name(news_source_name: NewsSourceNames):
        pass

    def get_news_source_status(self, news_source_name: NewsSourceNames):
        pass

    def switch_news_source_status(self, news_source_name: NewsSourceNames):
        pass

    def go_back_to_settings_page(self):
        pass


class NewsSourcePageANDROID(NewsSourcePage):

    def get_news_source_by_name(self, news_source_name: NewsSourceNames):
        locator = self.get_news_source_locator_by_name(news_source_name)
        return self.find(locator)

    @staticmethod
    def get_news_source_locator_by_name(news_source_name: NewsSourceNames):
        return NewsSourceLocatorMatching.get(news_source_name)

    def get_news_source_status(self, news_source_name: NewsSourceNames):
        news_source_locator = self.get_news_source_locator_by_name(news_source_name)
        full_locator = (
            news_source_locator[0],
            news_source_locator[1] + "/following-sibling::" + NewsSourcePageLocators.ITEM_SELECTED_MARKER[1][2:]
        )
        try:
            self.find(full_locator)
        except TimeoutException:
            return False
        return True

    def switch_news_source_status(self, news_source_name: NewsSourceNames):
        status_before = self.get_news_source_status(news_source_name)
        news_source = self.get_news_source_by_name(news_source_name)
        news_source.click()
        status_after = self.get_news_source_status(news_source_name)
        assert status_before or status_before != status_after

    def go_back_to_settings_page(self):
        back_button = self.find(NewsSourcePageLocators.BACK_BUTTON)
        back_button.click()
