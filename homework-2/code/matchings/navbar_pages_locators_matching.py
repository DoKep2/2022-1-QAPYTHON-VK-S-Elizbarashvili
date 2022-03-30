from enums.navbar_page_names import NavbarPageNames
from ui.locators.basic_locators import AuthorizedMainPageLocators as Locators

NavbarPagesLocatorsMatching = {
            NavbarPageNames.CAMPAIGNS: Locators.CAMPAIGNS_LINK,
            NavbarPageNames.AUDIENCES: Locators.AUDIENCES_LINK,
            NavbarPageNames.BILLING: Locators.BILLING_LINK,
            NavbarPageNames.STATISTICS: Locators.STATISTICS_LINK,
            NavbarPageNames.PRO: Locators.PRO_LINK,
            NavbarPageNames.PROFILE: Locators.PROFILE_LINK,
            NavbarPageNames.TOOLS: Locators.TOOLS_LINK,
            NavbarPageNames.HELP: Locators.HELP_LINK
            }
