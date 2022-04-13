from ui.locators.locators_android import RequestPermissionWindowLocators
from ui.pages import BasePage


class RequestPermissionWindow(BasePage):
    def allow_request_permission(self):
        pass


class RequestPermissionWindowANDROID(RequestPermissionWindow):
    def allow_request_permission(self):
        permission_allow_button = self.find(RequestPermissionWindowLocators.PERMISSION_ALLOW_BUTTON)
        permission_allow_button.click()
