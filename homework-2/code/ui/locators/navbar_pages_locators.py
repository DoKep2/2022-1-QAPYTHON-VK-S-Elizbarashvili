from selenium.webdriver.common.by import By


class CampaignsBasePageLocators:
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//div[contains(@class, 'dashboard-module-createButtonWrap')]/div/div")
    ADVERTISED_OBJECT_LINK_INPUT = (By.XPATH, "//input[@data-gtm-id = 'ad_url_text']")
    NOTIFY_SUCCESS_ICON = (By.XPATH, "//div[contains(@class, 'icon-success')]")

    class NewCampaignPageLocators:
        BANNER_FORMATS_MODULE = (By.XPATH, "//div[contains(@class, 'bannerFormats-module-formatsWrap')]")
        IMAGE_SAVE_BUTTON = (By.CSS_SELECTOR, ".image-cropper__save.js-save")
        TAB_MODULE_GREEN = (By.XPATH, "//div[contains(@class, 'patternTabs-module-green')]")
        SAVE_AD_BUTTON = (By.XPATH, "//div[@data-test='submit_banner_button']")
        PREVIEW_TABS_CONTAINER = (By.XPATH, "//div[contains(@class, 'bannerPreview-module-previewTabsContainer')]")
        CREATE_CAMPAIGN_BUTTON = (
            By.XPATH,
            "//div[@class='footer__button js-save-button-wrap']/button[@class='button button_submit']"
        )
        PRICE_SLIDER_SETTING_BUTTON = (By.CSS_SELECTOR, '.price-slider-setting__btn')
        CAMPAIGN_NAME_INPUT = (By.CSS_SELECTOR, '.input_campaign-name > * > *')

        class CampaignObjectivesButtonsLocators:
            TRAFFIC = (By.CSS_SELECTOR, "._traffic")
            APP_INSTALLS = (By.CSS_SELECTOR, "._appinstalls")
            MOBILE_APP_REENGAGEMENT = (By.CSS_SELECTOR, "._reengagements")
            SOCIAL_ENGAGEMENT = (By.CSS_SELECTOR, "._socialengagement")
            SOCIAL_GAMES_ENGAGEMENT = (By.CSS_SELECTOR, "._playersengagement")
            CATALOGUE_SALES = (By.CSS_SELECTOR, "._storeproductssales")
            STORE_VISITS = (By.CSS_SELECTOR, "._storevisits")
            REACH = (By.CSS_SELECTOR, "._reach")
            VIDEO_VIEWS = (By.CSS_SELECTOR, "._videoviews")
            AUDIO_LISTENING = (By.CSS_SELECTOR, "._audiolistening")
            SPECIAL = (By.CSS_SELECTOR, "._special")
            VK_PRODUCTS = (By.CSS_SELECTOR, "._general_ttm")
            DOOH = (By.CSS_SELECTOR, "._dooh")
            INDOOR_ADVERTISING = (By.CSS_SELECTOR, "._indoor")

        class BannerFormatsLocators:
            CAROUSEL = (By.XPATH, "//div[contains(@id, 'patterns_carousel')]")
            MULTIFORMAT = (By.XPATH, "//div[contains(@id, 'patterns_multi')]")
            SQUARE_VIDEO = (By.XPATH, "//div[contains(@id, 'patterns_squarevideo')]")
            HORIZONTAL_VIDEO = (By.XPATH, "//div[contains(@id, 'patterns_rectanglevideo')]")
            INTERSTITIAL_VIDEO = (By.XPATH, "//div[contains(@id, 'patterns_fullscreen')]")
            BANNER = (By.XPATH, "//div[contains(@id, 'patterns_banner')]")
            TEASER = (By.XPATH, "//div[contains(@id, 'patterns_teaser')]")

        class BannersLocators:
            class Carousel:
                pass

            class Multiformat:
                pass

            class SquareVideo:
                pass

            class HorizontalVideo:
                pass

            class InterstitialVideo:
                pass

            class Banner:
                IMAGE_UPLOAD_BUTTON = (
                    By.XPATH,
                    "//div[contains(@class, 'roles-module-buttonWrap')]//div[contains(@class, "
                    "'upload-module-wrapper')]//input "
                )

            class Teaser:
                pass


class AudiencesBasePageLocators:
    CREATE_SEGMENT_LINK = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    CREATE_SEGMENT_BUTTON = (By.CSS_SELECTOR, "button.button_submit")
    SEGMENTS_LIST_SPAN = (
        By.XPATH,
        "//a[@href='/segments/segments_list']/span[@class='left-nav__count js-nav-item-count']"
    )
    CONFIRM_DELETION_BUTTON = (By.CSS_SELECTOR, ".button.button_confirm-remove .button__text")
    FIRST_SEGMENT_SPAN = (
        By.XPATH,
        "(//input[contains(@class, 'segmentsTable-module-idCellCheckbox')]/following-sibling::span)[1]"
    )
    SEARCH_INPUT = (By.XPATH, '//input[contains(@class, "suggester-module-searchInput")]')
    SUGGESTER_MODULE_OPTION = (By.XPATH, '//li[contains(@class, "suggester-module-option")]')

    class NewSegmentModalPanelLocators:
        ADD_SEGMENT_BUTTON = (By.CSS_SELECTOR, "div.adding-segments-modal__btn-wrap button.button.button_submit")
        CLOSE_BUTTON = (By.CSS_SELECTOR, "button.button.button_general")
        PLAYED_AND_PAID_CHECKBOX = (By.CSS_SELECTOR, "input.adding-segments-source__checkbox")
        APPS_AND_GAMES_ITEM = (By.XPATH, "//div[contains(@class, 'adding-segments-item')] [8]")

    class NewSegmentPageLocators:
        CREATE_SEGMENT_BUTTON = (By.CSS_SELECTOR, ".button__text")
        SEGMENT_NAME_INPUT = (By.CSS_SELECTOR, '.input_create-segment-form > * > *')


class BillingPageLocators:
    pass


class StatisticsPageLocators:
    pass


class ProPageLocators:
    pass


class ProfilePageLocators:
    pass


class ToolsPageLocators:
    pass


class HelpPageLocators:
    pass
