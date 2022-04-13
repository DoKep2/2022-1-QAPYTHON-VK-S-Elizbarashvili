import os

from ui.locators.locators_android import AboutPageLocators
from ui.pages import BasePage


class AboutPage(BasePage):
    def get_apk_version(self, repo_root):
        pass

    def check_version(self, repo_root):
        pass

    def trademark_is_present(self):
        pass


class AboutPageANDROID(AboutPage):
    def get_apk_version(self, repo_root):
        from os import listdir
        from os.path import isfile, join
        apk_path = os.path.join(repo_root, "stuff")
        files_names = [f for f in listdir(apk_path) if isfile(join(apk_path, f))]
        apk_file_name = files_names[0]
        apk_version = apk_file_name.split(' ')[0].split('_')[1][1:]
        return apk_version

    def check_version(self, repo_root):
        apk_version = self.get_apk_version(repo_root)
        version_title = self.find(AboutPageLocators.VERSION_TITLE)
        app_version = version_title.text.split(' ')[1]
        assert apk_version == app_version

    def trademark_is_present(self):
        self.is_element_present(AboutPageLocators.TRADE_MARK)


