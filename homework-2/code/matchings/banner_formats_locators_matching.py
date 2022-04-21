from enums.banner_format_names import BannerFormatNames as Names
from ui.locators.navbar_pages_locators import CampaignsBasePageLocators as Locators

loc = Locators.NewCampaignPageLocators.BannerFormatsLocators

BannerFormatsLocatorsMatching = {
    Names.CAROUSEL: loc.CAROUSEL,
    Names.MULTIFORMAT: loc.MULTIFORMAT,
    Names.SQUARE_VIDEO: loc.SQUARE_VIDEO,
    Names.HORIZONTAL_VIDEO: loc.HORIZONTAL_VIDEO,
    Names.BANNER: loc.BANNER,
    Names.TEASER: loc.TEASER,
}