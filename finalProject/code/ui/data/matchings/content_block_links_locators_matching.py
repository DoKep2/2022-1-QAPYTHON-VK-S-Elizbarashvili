from ui.data.enums.block_links_names import BlockLinksNames
from ui.locators.main_page_locators import MainPageLocators

ContentBlockLinksLocatorsMatching = {
    BlockLinksNames.API: MainPageLocators.ContentBlockLocators.API_IMAGE,
    BlockLinksNames.INTERNET: MainPageLocators.ContentBlockLocators.INTERNET_IMAGE,
    BlockLinksNames.SMTP: MainPageLocators.ContentBlockLocators.SMPT_IMAGE
}
