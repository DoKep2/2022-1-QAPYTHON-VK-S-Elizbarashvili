from selenium.webdriver.common.by import By


class AuthorizedMainPageLocators:
    LOG_OUT_BUTTON = (By.XPATH, "//a[@class='rightMenu-module-rightMenuLink-2j8bjX' and @href='/logout']")
    RIGHT_MODULE_BUTTON = (By.CSS_SELECTOR, ".right-module-rightButton-3e-duF.right-module-mail-aXwV1G")
    CAMPAIGNS_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-campaigns-3KazFg' and @href='/dashboard']")
    AUDIENCES_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-segments-1MqckW' and @href='/segments']")
    BILLING_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-billing-1cIfj4' and @href='/billing']")
    STATISTICS_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-statistics-2Wbrwh' and @href='/statistics']")
    PRO_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-pro-1lbACy' and @href]")
    PROFILE_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-profile-1kuUOa' and @href='/profile']")
    TOOLS_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-tools-dypAE6' and @href='/tools']")
    HELP_LINK = \
        (By.XPATH, "//a[@class='center-module-button-14O4yB center-module-help-2k80UI' and @href]")


class ProfilePageLocators:
    FULL_NAME_INPUT = (By.CSS_SELECTOR, "div[data-name='fio']  input.input__inp.js-form-element")
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, "div[data-name='phone']  input.input__inp.js-form-element")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".button__text")


class LogInModalPanelLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='authForm-module-button-1u2DYF']")


class UnauthorizedMainPageLocators:
    LOG_IN_BUTTON = (By.CSS_SELECTOR, ".responseHead-module-button-2yl51i")