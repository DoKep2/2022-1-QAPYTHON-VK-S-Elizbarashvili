import pytest


@pytest.mark.UI
def test_user_can_create_segment(browser, audiences_page):
    page = audiences_page
    page.create_segment()


@pytest.mark.UI
def test_user_can_delete_segment(audiences_page):
    page = audiences_page
    page.delete_segment()
