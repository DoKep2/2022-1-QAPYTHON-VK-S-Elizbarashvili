from ui.locators.locators_android import AboutPageLocators
from ui.pages import BasePage


class AboutPage(BasePage):

    def check_version(self, repo_root, get_apk_version):
        pass

    def trademark_is_present(self):
        pass


class AboutPageANDROID(AboutPage):

    def check_version(self, repo_root, get_apk_version):
        apk_version = get_apk_version
        version_title = self.find(AboutPageLocators.VERSION_TITLE)
        app_version = version_title.text.split(' ')[1]
        assert apk_version == app_version

    def trademark_is_present(self):
        self.is_element_present(AboutPageLocators.TRADE_MARK)


