import os

from enums.campaign_objective_names import CampaignObjectiveNames
from ui.input_data_generator import MyFaker
from ui.locators.navbar_pages_locators import CampaignsBasePageLocators as Base
from ui.pages.navbar_pages.navbar_page import NavbarPage
from matchings.campaign_objectives_locators_matching import CampaignObjectivesLocatorsMatching
from matchings.banner_formats_locators_matching import BannerFormatsLocatorsMatching
from selenium.webdriver.support import expected_conditions as EC


class CampaignsPage(NavbarPage):
    def go_to_campaign_creation_page(self):
        create_campaign_btn = self.find(Base.CREATE_CAMPAIGN_BUTTON)
        create_campaign_btn.click()
        assert self.browser.current_url == "https://target.my.com/campaign/new"

    def choose_campaign_objective(self, name: CampaignObjectiveNames):
        locator = CampaignObjectivesLocatorsMatching.get(name)
        self.find(locator).click()

    def enter_advertised_object_link(self):
        link_input = self.find(Base.ADVERTISED_OBJECT_LINK_INPUT)
        link_input.send_keys(MyFaker.fake_url())

    def choose_format(self, banner_format):
        banner_formats = self.find(Base.NewCampaignPageLocators.BANNER_FORMATS_MODULE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", banner_formats)
        locator = BannerFormatsLocatorsMatching.get(banner_format)
        self.find(locator).click()

    def upload_photo(self, repo_root):
        photo = os.path.join(repo_root, "files")
        photo = os.path.join(photo, "kitty.jpg")
        image_upload_btn = self.find(Base.NewCampaignPageLocators.BannersLocators.Banner.IMAGE_UPLOAD_BUTTON)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", image_upload_btn)
        image_upload_btn.send_keys(photo)
        image_save_btn = self.find(Base.NewCampaignPageLocators.IMAGE_SAVE_BUTTON)
        image_save_btn.click()
        self.photo_is_uploaded()

    def save_changes(self):
        save_ad_btn = self.find(Base.NewCampaignPageLocators.SAVE_AD_BUTTON)
        save_ad_btn.click()
        assert self.is_element_present(Base.NewCampaignPageLocators.PREVIEW_TABS_CONTAINER)

    def wait_slider_loading(self, timeout=10):
        slider = Base.NewCampaignPageLocators.PRICE_SLIDER_SETTING_BUTTON
        self.wait(timeout).until(EC.visibility_of_element_located(slider))

    def create_campaign(self, name=MyFaker.fake_name()):

        campaign_name_input = self.find(Base.NewCampaignPageLocators.CAMPAIGN_NAME_INPUT)
        campaign_name_input.clear()
        campaign_name_input.send_keys(name)
        self.wait_slider_loading()
        create_campaign_button = self.find(Base.NewCampaignPageLocators.CREATE_CAMPAIGN_BUTTON)
        create_campaign_button.click()

    def photo_is_uploaded(self):
        assert self.is_element_present(Base.NewCampaignPageLocators.TAB_MODULE_GREEN), "photo isn't uploaded"

    def campaign_was_created(self):
        assert self.is_element_present(Base.NOTIFY_SUCCESS_ICON), "campaign wasn't created"




