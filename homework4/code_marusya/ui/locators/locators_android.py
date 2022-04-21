from appium.webdriver.common.mobileby import MobileBy


class RequestPermissionWindowLocators:
    PERMISSION_ALLOW_BUTTON = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
    PERMISSION_DENY_BUTTON = (MobileBy.ID, 'com.android.packageinstaller:id/permission_deny_button')


class BasePageLocators:
    pass


class MainPageLocators(BasePageLocators):
    KEYBOARD_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    QUESTION_INPUT = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    SUBMIT_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_action')
    RESPONSE_BLOCK = (
        MobileBy.XPATH,
        '//android.widget.TextView[@resource-id="ru.mail.search.electroscope:id/dialog_item"]'
    )
    SUGGEST_CAROUSEL = (MobileBy.ID, 'ru.mail.search.electroscope:id/suggests_list')
    SUGGEST_ITEMS = (MobileBy.XPATH, '//android.widget.TextView')
    FACT_CARD_TITLE = (MobileBy.XPATH, '//android.widget.TextView[contains(@text, "{}")]')
    DIALOG_ITEM = (
        MobileBy.XPATH,
        '//android.widget.TextView[contains(@text, "{}")]'
    )
    ASSISTANT_MENU_BUTTON = (MobileBy.ID, "ru.mail.search.electroscope:id/assistant_menu_bottom")


class SettingsPageLocators(BasePageLocators):
    NEWS_SOURCE_FIELD = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    CLOSE_BUTTON = (
        MobileBy.XPATH,
        '//android.widget.LinearLayout[@resource-id="ru.mail.search.electroscope:id/user_settings_toolbar"]//android'
        '.widget.ImageButton'
    )
    ABOUT_FIELD = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')


class NewsSourcePageLocators(BasePageLocators):
    MAIL_RU_NEWS = (MobileBy.XPATH, '//android.widget.TextView[contains(@text, "Новости Mail.ru")]')
    COMMERSANT_FM = (MobileBy.XPATH, '//android.widget.TextView[contains(@text, "Коммерсант FM")]')
    GAZETA_RU = (MobileBy.XPATH, '//android.widget.TextView[contains(@text, "Газета.Ru")]')
    ITEM_SELECTED_MARKER = (
        MobileBy.XPATH,
        '//android.widget.ImageView[@resource-id="ru.mail.search.electroscope:id/news_sources_item_selected"]'
    )
    BACK_BUTTON = (MobileBy.XPATH, '//android.widget.ImageButton')


class AboutPageLocators(BasePageLocators):
    VERSION_TITLE = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_version')
    TRADE_MARK = (MobileBy.XPATH, '//*[contains(@text, "Все права защищены.")]')
