from ui.locators.locators_android import MainPageLocators
from ui.pages.base_page import BasePage

ASK_ATTEMPTS = 5


class MainPage(BasePage):
    def ask_Marusya(self, text, expected_answer_title):
        pass

    def response_is_present(self, request_text):
        pass

    def response_is_correct(self, locator, expected_text):
        pass

    def choose_question_from_suggest_carousel(self, question_text, expected_answer):
        pass

    def compute_expression(self, math_expression):
        pass

    def go_to_settings_page(self):
        pass


class MainPageANDROID(MainPage):

    def click_keyboard_button(self):
        keyboard_button = self.find(MainPageLocators.KEYBOARD_BUTTON)
        keyboard_button.click()

    def ask_Marusya(self, text, expected_answer_title):
        self.click_keyboard_button()
        is_present = False
        for i in range(ASK_ATTEMPTS):
            question_input = self.find(MainPageLocators.QUESTION_INPUT)
            question_input.send_keys(text)
            submit_button = self.find(MainPageLocators.SUBMIT_BUTTON)
            submit_button.click()
            self.driver.hide_keyboard()
            if self.response_is_present(text):
                is_present = True
                break
        assert is_present
        assert self.response_is_correct(MainPageLocators.FACT_CARD_TITLE, expected_answer_title)

    def response_is_present(self, request_text):
        return self.driver.find_elements(*MainPageLocators.RESPONSE_BLOCK)[-1].text != request_text

    def response_is_correct(self, locator, expected_text):
        return self.is_element_present(self.locator_format(locator, expected_text))

    def choose_question_from_suggest_carousel(self, request_text, expected_answer):
        suggest_item = self.horizontal_swipe_to_element_with_correspondent_text(
            MainPageLocators.SUGGEST_CAROUSEL,
            MainPageLocators.SUGGEST_ITEMS,
            request_text
        )
        suggest_item.click()
        self.response_is_present(request_text)
        self.response_is_correct(MainPageLocators.DIALOG_ITEM, expected_answer)

    def compute_expression(self, math_expression):
        self.click_keyboard_button()
        question_input = self.find(MainPageLocators.QUESTION_INPUT)
        question_input.send_keys(math_expression)
        submit_button = self.find(MainPageLocators.SUBMIT_BUTTON)
        submit_button.click()
        expected_result = str(eval(math_expression))
        self.response_is_correct(MainPageLocators.DIALOG_ITEM, expected_result)

    def go_to_settings_page(self):
        assistant_menu_button = self.find(MainPageLocators.ASSISTANT_MENU_BUTTON)
        assistant_menu_button.click()