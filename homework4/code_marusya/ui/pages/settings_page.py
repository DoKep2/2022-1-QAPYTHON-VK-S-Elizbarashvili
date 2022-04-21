from ui.locators.locators_android import SettingsPageLocators
from ui.pages import BasePage


class SettingsPage(BasePage):
    def go_to_news_source_page(self):
        pass

    def go_to_about_page(self):
        pass

    def close_settings_page(self):
        pass


class SettingsPageANDROID(SettingsPage):
    def go_to_news_source_page(self):
        self.vertical_swipe_to_element(SettingsPageLocators.NEWS_SOURCE_FIELD, 10)
        news_source_field = self.find(SettingsPageLocators.NEWS_SOURCE_FIELD)
        news_source_field.click()

    def close_settings_page(self):
        close_button = self.find(SettingsPageLocators.CLOSE_BUTTON)
        close_button.click()

    def go_to_about_page(self):
        self.vertical_swipe_to_element(SettingsPageLocators.ABOUT_FIELD, 10)
        about_field = self.find(SettingsPageLocators.ABOUT_FIELD)
        about_field.click()