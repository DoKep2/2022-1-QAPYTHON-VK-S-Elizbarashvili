import faker

from ui import input_data_generator
from ui.locators.basic_locators import ProfilePageLocators
from ui.pages.navbar_pages.navbar_page import NavbarPage


class ProfilePage(NavbarPage):
    def change_full_name(self):
        full_name_input = self.find(ProfilePageLocators.FULL_NAME_INPUT)
        full_name_input.clear()
        f = faker.Faker()
        fake_name = input_data_generator.fake_name(f)
        full_name_input.send_keys(fake_name)
        save_btn = self.find(ProfilePageLocators.SAVE_BUTTON)
        save_btn.click()

    def change_phone_number(self):
        phone_number_input = self.find(ProfilePageLocators.PHONE_NUMBER_INPUT)
        phone_number_input.clear()
        f = faker.Faker()
        fake_phone_number = input_data_generator.fake_phone_number(f)
        phone_number_input.send_keys(fake_phone_number)
        save_btn = self.find(ProfilePageLocators.SAVE_BUTTON)
        save_btn.click()
