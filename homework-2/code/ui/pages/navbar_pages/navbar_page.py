from matchings.navbar_pages_links_matching import NavbarPagesLinksMatching
from matchings.navbar_pages_locators_matching import NavbarPagesLocatorsMatching
from ui.pages.basic_pages.authorized_main_page import AuthorizedMainPage
from enums.navbar_page_names import NavbarPageNames


class NavbarPage(AuthorizedMainPage):
    def go_to_navbar_page(self, page_name: NavbarPageNames):
        locator = NavbarPagesLocatorsMatching.get(page_name)
        self.find(locator).click()

    def transition_is_correct(self, page_name: NavbarPageNames):
        link = self.browser.current_url
        assert (link, page_name) in NavbarPagesLinksMatching.items(), f"{link} {page_name}"



