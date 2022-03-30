from ui.pages.navbar_pages.navbar_page import NavbarPage
from ui.locators.navbar_pages_locators import AudiencesBasePageLocators
from ...locators.basic_locators import get_data_locator_by_action_and_id

loc = AudiencesBasePageLocators.NewSegmentModalPanelLocators


class AudiencesPage(NavbarPage):
    def create_segment(self):
        current_segments_amount = self.get_current_segments_list_size()
        if current_segments_amount == 0:
            create_segment_btn = self.find(AudiencesBasePageLocators.CREATE_SEGMENT_LINK)
        else:
            create_segment_btn = self.find(AudiencesBasePageLocators.CREATE_SEGMENT_BUTTON)
        create_segment_btn.click()
        apps_and_games_item = self.find(loc.APPS_AND_GAMES_ITEM)
        apps_and_games_item.click()
        played_and_paid_checkbox = self.find(loc.PLAYED_AND_PAID_CHECKBOX)
        played_and_paid_checkbox.click()
        add_segment_btn = self.find(loc.ADD_SEGMENT_BUTTON)
        add_segment_btn.click()
        create_segment_btn = self.find(AudiencesBasePageLocators.NewSegmentPageLocators.CREATE_SEGMENT_BUTTON)
        create_segment_btn.click()
        self.segments_list_has_correspondent_size(current_segments_amount + 1)

    def delete_segment(self):
        current_segments_amount = self.get_current_segments_list_size()
        self.create_segment()
        segment_remove_btn = self.find(get_data_locator_by_action_and_id('remove', self.get_first_segment_id()))
        segment_remove_btn.click()
        self.confirm_deletion()
        self.segments_list_has_correspondent_size(current_segments_amount)

    def get_first_segment_id(self):
        first_segment_span = self.find(AudiencesBasePageLocators.FIRST_SEGMENT_SPAN)
        segment_id = first_segment_span.text
        return segment_id

    def confirm_deletion(self):
        delete_btn = self.find(AudiencesBasePageLocators.CONFIRM_DELETION_BUTTON)
        delete_btn.click()

    def get_current_segments_list_size(self):
        segments_list_span = self.find(AudiencesBasePageLocators.SEGMENTS_LIST_SPAN)
        return int(segments_list_span.text)

    def segments_list_has_correspondent_size(self, size):
        return self.is_text_presented(AudiencesBasePageLocators.SEGMENTS_LIST_SPAN, str(size))
