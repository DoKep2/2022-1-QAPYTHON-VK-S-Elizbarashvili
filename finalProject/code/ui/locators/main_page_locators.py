from selenium.webdriver.common.by import By


class MainPageLocators:
    class NavbarLinksLocators:
        HOME_LINK = (By.XPATH, "//a[contains(@class, 'uk-navbar-brand') and @href='/']")
        HOME_LINK_2 = (By.XPATH, "//li/a[@href='/']")
        PYTHON_LINK = (By.XPATH, "//a[@href='https://www.python.org/']")
        PYTHON_HISTORY_LINK = (By.XPATH, "//a[@href='https://en.wikipedia.org/wiki/History_of_Python']")
        ABOUT_FLASK_LINK = (By.XPATH, "//a[@href='https://flask.palletsprojects.com/en/1.1.x/#']")
        DOWNLOAD_CENTOS_LINK = (By.XPATH, "//a[@href='https://getfedora.org/ru/workstation/download/']")
        NETWORK_WIRESHARK_NEWS_LINK = (By.XPATH, "//a[@href='https://www.wireshark.org/news/']")
        NETWORK_WIRESHARK_DOWNLOAD_LINK = (By.XPATH, "//a[@href='https://www.wireshark.org/#download']")
        NETWORK_TCPDUMP_EXAMPLES_LINK = (By.XPATH, "//a[@href='https://hackertarget.com/tcpdump-examples/']")
        LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    class NavbarDropdownButtonsLocators:
        PYTHON_BUTTON = (By.XPATH, "//li[@class='uk-parent'][1]/a")
        LINUX_BUTTON = (By.XPATH, "//li[@class='uk-parent'][2]/a")
        NETWORK_BUTTON = (By.XPATH, "//li[@class='uk-parent'][3]/a")

    class ContentBlockLocators:
        API_IMAGE = (By.XPATH, "//img[@src='/static/images/laptop.png']")
        INTERNET_IMAGE = (By.XPATH, "//img[@src='/static/images/loupe.png']")
        SMPT_IMAGE = (By.XPATH, "//img[@src='/static/images/analytics.png']")

    class ProfileLocators:
        USER_TEXT = (By.CSS_SELECTOR, '#login-name > ul > li:nth-child(2)')
        VK_ID_TEXT = (By.CSS_SELECTOR, '#login-name > ul > li:nth-child(3)')
