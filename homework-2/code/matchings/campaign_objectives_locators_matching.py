from enums.campaign_objective_names import CampaignObjectiveNames as Names
from ui.locators.navbar_pages_locators import CampaignsBasePageLocators as Locators

loc = Locators.NewCampaignPageLocators.CampaignObjectivesButtonsLocators

CampaignObjectivesLocatorsMatching = {
    Names.TRAFFIC: loc.TRAFFIC,
    Names.APP_INSTALLS: loc.APP_INSTALLS,
    Names.MOBILE_APP_REENGAGEMENT: loc.MOBILE_APP_REENGAGEMENT,
    Names.SOCIAL_ENGAGEMENT: loc.SOCIAL_ENGAGEMENT,
    Names.SOCIAL_GAMES_ENGAGEMENT: loc.SOCIAL_GAMES_ENGAGEMENT,
    Names.CATALOGUE_SALES: loc.CATALOGUE_SALES,
    Names.STORE_VISITS: loc.STORE_VISITS,
    Names.REACH: loc.REACH,
    Names.VIDEO_VIEWS: loc.VIDEO_VIEWS,
    Names.AUDIO_LISTENING: loc.AUDIO_LISTENING,
    Names.SPECIAL: loc.SPECIAL,
    Names.VK_PRODUCTS: loc.VK_PRODUCTS,
    Names.DOOH: loc.DOOH,
    Names.INDOOR_ADVERTISING: loc.INDOOR_ADVERTISING,
}