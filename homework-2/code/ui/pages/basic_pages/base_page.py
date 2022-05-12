import time

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CLICK_RETRY = 3
DEFAULT_TIME_TO_WAIT_SEC = 15


class BasePage:
    def __init__(self, browser, url, timeout=DEFAULT_TIME_TO_WAIT_SEC):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click(self, locator):
        for i in range(CLICK_RETRY):
            time.sleep(1)
            try:
                self.find(locator, DEFAULT_TIME_TO_WAIT_SEC)
                elem = self.wait(DEFAULT_TIME_TO_WAIT_SEC).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except WebDriverException:
                if i == CLICK_RETRY - 1:
                    raise

    def find(self, locator, timeout=DEFAULT_TIME_TO_WAIT_SEC):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.find(locator)
        except WebDriverException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=DEFAULT_TIME_TO_WAIT_SEC):
        try:
            self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_text_presented(self, locator, text, timeout=DEFAULT_TIME_TO_WAIT_SEC):
        try:
            self.wait(timeout).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False
        return True

    def wait(self, timeout=None):
        if timeout is None:
            timeout = DEFAULT_TIME_TO_WAIT_SEC
        return WebDriverWait(self.browser, timeout=timeout)

