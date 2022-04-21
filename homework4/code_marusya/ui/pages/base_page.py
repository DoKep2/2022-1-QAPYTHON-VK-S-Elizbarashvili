from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.locators_android import RequestPermissionWindowLocators

CLICK_RETRY = 3
BASE_TIMEOUT = 5


class PageNotLoadedException(Exception):
    pass


class BasePage(object):

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def allow_request_permission(self):
        permission_allow_button = self.find(RequestPermissionWindowLocators.PERMISSION_ALLOW_BUTTON)
        permission_allow_button.click()

    @staticmethod
    def locator_format(locator, text):
        return locator[0], locator[1].format(text)

    def is_element_present(self, locator):
        try:
            self.find(locator)
        except WebDriverException:
            return False
        return True

    def find(self, locator, timeout=BASE_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @property
    def action_chains(self):
        return ActionChains(self.driver)
    ###??????

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def click_for_android(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def swipe_up(self, swipetime=200):
        """
        Базовый метод свайпа по вертикали
        Описание работы:
        1. узнаем размер окна телефона
        2. Задаем за X - центр нашего экрана
        3. Указываем координаты откуда и куда делать свайп
        4. TouchAction нажимает на указанные стартовые координаты, немного ждет и передвигает нас из одной точки в другую.
        5. release() наши пальцы с экрана, а perform() выполняет всю эту цепочку команд.
        """
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    def vertical_swipe_to_element(self, locator, max_swipes):
        """
        :param locator: локатор, который мы ищем
        :param max_swipes: количество свайпов до момента, пока тест не перестанет свайпать вверх
        """
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator}, please check function")
            self.swipe_up()
            already_swiped += 1

    def horizontal_swipe_to_element_with_correspondent_text(self, carousel_locator, locator, text):
        # XPATH with <contains(text())> doesn't work with сyrillic
        while self.driver.find_elements(*locator)[-1].text != text:
            self.swipe_element_lo_left(carousel_locator, 200)
        return self.driver.find_elements(*locator)[-1]

    def swipe_element_lo_left(self, locator, distance=None):
        """
        :param locator: локатор, который мы ищем
        :param distance: дистанция в пикселях на которую свапаем
        1. Находим наш элемент на экране
        2. Получаем его координаты (начала, конца по ширине и высоте)
        3. Находим центр элемента (по высоте)
        4. Делаем свайп влево, двигая центр элемента за его правую часть в левую сторону.
        """
        web_element = self.find(locator, 10)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width'] - 1
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        destination_x = right_x - distance
        if distance is None:
            destination_x = left_x
        action = TouchAction(self.driver)
        action. \
            press(x=right_x, y=middle_y). \
            wait(ms=300). \
            move_to(x=destination_x, y=middle_y). \
            release(). \
            perform()