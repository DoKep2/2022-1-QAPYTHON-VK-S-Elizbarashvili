from ui.data.enums.block_links_names import BlockLinksNames
from ui.data.enums.navbar_links_names import NavbarLinksNames
from ui.data.matchings.content_block_links_locators_matching import ContentBlockLinksLocatorsMatching
from ui.data.matchings.content_block_links_urls_matching import ContentBlockLinksUrlsMatching
from ui.data.matchings.navbar_links_dropdown_buttons_matching import NavbarLinksDropdownButtonsMatching
from ui.data.matchings.navbar_links_locators_matching import NavbarLinksLocatorsMatching
from ui.data.matchings.navbar_links_urls_matching import NavbarLinksUrlsMatching
from ui.locators.main_page_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    def logout(self):
        self.find(MainPageLocators.NavbarLinksLocators.LOGOUT_BUTTON).click()

    def vk_id_is_presented(self):
        return self.is_element_present(MainPageLocators.ProfileLocators.VK_ID_TEXT)

    def go_navbar_link(self, link_name: NavbarLinksNames):
        self.move_cursor_to_element(self.find(NavbarLinksDropdownButtonsMatching.get(link_name)))
        self.find(NavbarLinksLocatorsMatching.get(link_name)).click()
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def navbar_link_transition_is_correct(self, page_name: NavbarLinksNames):
        link = self.browser.current_url
        assert (link, page_name) in NavbarLinksUrlsMatching.items(), f"{link} {page_name}"

    def go_to_content_block_page(self, link_name: BlockLinksNames):
        self.find(ContentBlockLinksLocatorsMatching.get(link_name)).click()
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def block_link_transition_is_correct(self, link_name: BlockLinksNames):
        link = self.browser.current_url
        assert (link, link_name) in ContentBlockLinksUrlsMatching.items(), f"{link} {link_name}"
