from ui.data.enums.navbar_links_names import NavbarLinksNames
from ui.locators.main_page_locators import MainPageLocators

NavbarLinksDropdownButtonsMatching = {
    NavbarLinksNames.PYTHON_HISTORY: MainPageLocators.NavbarDropdownButtonsLocators.PYTHON_BUTTON,
    NavbarLinksNames.FLASK: MainPageLocators.NavbarDropdownButtonsLocators.PYTHON_BUTTON,
    NavbarLinksNames.CENTOS: MainPageLocators.NavbarDropdownButtonsLocators.LINUX_BUTTON,
    NavbarLinksNames.WIRESHARK_NEWS: MainPageLocators.NavbarDropdownButtonsLocators.NETWORK_BUTTON,
    NavbarLinksNames.WIRESHARK_DOWNLOAD: MainPageLocators.NavbarDropdownButtonsLocators.NETWORK_BUTTON,
    NavbarLinksNames.TCPDUMP_EXAMPLES: MainPageLocators.NavbarDropdownButtonsLocators.NETWORK_BUTTON,
}
