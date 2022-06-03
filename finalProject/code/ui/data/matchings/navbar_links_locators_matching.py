from ui.data.enums.navbar_links_names import NavbarLinksNames
from ui.locators.main_page_locators import MainPageLocators

NavbarLinksLocatorsMatching = {
    NavbarLinksNames.HOME: MainPageLocators.NavbarLinksLocators.HOME_LINK,
    NavbarLinksNames.HOME_2: MainPageLocators.NavbarLinksLocators.HOME_LINK_2,
    NavbarLinksNames.PYTHON: MainPageLocators.NavbarLinksLocators.PYTHON_LINK,
    NavbarLinksNames.PYTHON_HISTORY: MainPageLocators.NavbarLinksLocators.PYTHON_HISTORY_LINK,
    NavbarLinksNames.FLASK: MainPageLocators.NavbarLinksLocators.ABOUT_FLASK_LINK,
    NavbarLinksNames.CENTOS: MainPageLocators.NavbarLinksLocators.DOWNLOAD_CENTOS_LINK,
    NavbarLinksNames.WIRESHARK_NEWS: MainPageLocators.NavbarLinksLocators.NETWORK_WIRESHARK_NEWS_LINK,
    NavbarLinksNames.WIRESHARK_DOWNLOAD: MainPageLocators.NavbarLinksLocators.NETWORK_WIRESHARK_DOWNLOAD_LINK,
    NavbarLinksNames.TCPDUMP_EXAMPLES: MainPageLocators.NavbarLinksLocators.NETWORK_TCPDUMP_EXAMPLES_LINK,
}
