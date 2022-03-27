from navbar_pages_links_matching import matching
from ui.locators.basic_locators import AuthorizedMainPageLocators
from ui.pages.authorized_main_page import AuthorizedMainPage
from navbar_page_names import NavbarPageNames


class NavbarPage(AuthorizedMainPage):
    def go_to_navbar_page(self, page_name: NavbarPageNames):
        if page_name.name == NavbarPageNames.CAMPAIGNS:
            self.find(AuthorizedMainPageLocators.CAMPAIGNS_LINK).click()
        elif page_name == NavbarPageNames.AUDIENCES:
            self.find(AuthorizedMainPageLocators.AUDIENCES_LINK).click()
        elif page_name == NavbarPageNames.BILLING:
            self.find(AuthorizedMainPageLocators.BILLING_LINK).click()
        elif page_name == NavbarPageNames.STATISTICS:
            self.find(AuthorizedMainPageLocators.STATISTICS_LINK).click()
        elif page_name == NavbarPageNames.PRO:
            self.find(AuthorizedMainPageLocators.PRO_LINK).click()
        elif page_name == NavbarPageNames.PROFILE:
            self.find(AuthorizedMainPageLocators.PROFILE_LINK).click()
        elif page_name == NavbarPageNames.TOOLS:
            self.find(AuthorizedMainPageLocators.TOOLS_LINK).click()
        elif page_name == NavbarPageNames.HELP:
            self.find(AuthorizedMainPageLocators.HELP_LINK).click()

    def transition_is_correct(self, page_name: NavbarPageNames):
        link = self.browser.current_url
        assert (link, page_name) in matching.items(), f"{link} {page_name}"



