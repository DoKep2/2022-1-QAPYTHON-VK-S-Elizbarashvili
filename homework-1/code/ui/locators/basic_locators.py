from selenium.webdriver.common.by import By


class AuthorizedMainPageLocators:
    LOG_OUT_BUTTON = (By.XPATH, "//a[contains(@class, 'rightMenu-module-rightMenuLink') and @href='/logout']")
    RIGHT_MODULE_BUTTON = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
    CAMPAIGNS_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-campaigns')]")
    AUDIENCES_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-segments')]")
    BILLING_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-billing')]")
    STATISTICS_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-statistics')]")
    PRO_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-pro')]")
    PROFILE_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-profile')]")
    TOOLS_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-tools')]")
    HELP_LINK = \
        (By.XPATH, "//a[contains(@class, 'center-module-help')]")


class ProfilePageLocators:
    FULL_NAME_INPUT = (By.CSS_SELECTOR, "div[data-name='fio']  input.input__inp.js-form-element")
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, "div[data-name='phone']  input.input__inp.js-form-element")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".button__text")


class LogInModalPanelLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")


class UnauthorizedMainPageLocators:
    LOG_IN_BUTTON = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")