import pytest

from enums.campaign_objective_names import CampaignObjectiveNames
from enums.banner_format_names import BannerFormatNames


@pytest.mark.UI
@pytest.mark.parametrize("campaign_objective, banner_format",
                         [
                             (CampaignObjectiveNames.TRAFFIC, BannerFormatNames.BANNER),
                         ])
def test_user_can_create_campaign(browser, campaigns_page, campaign_objective, banner_format, repo_root):
    page = campaigns_page
    page.go_to_campaign_creation_page()
    page.choose_campaign_objective(campaign_objective)
    page.enter_advertised_object_link()
    page.choose_format(banner_format)
    page.upload_photo(repo_root)
    page.save_changes()
    page.create_campaign()
    page.campaign_was_created()


