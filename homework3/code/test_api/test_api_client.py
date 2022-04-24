import pytest

SOME_AUTHORIZED_PAGE_URL = "https://target.my.com/profile/contacts"


class TestApi:

    @pytest.mark.API
    def test_login(self, api_client):
        api_client.session.get(url=SOME_AUTHORIZED_PAGE_URL)

    @pytest.mark.API
    def test_create_segment(self, api_client):
        api_client.add_segment()

    @pytest.mark.API
    def test_delete_random_existing_segment(self, api_client):
        segment_id = api_client.get_random_existing_segment_id()
        api_client.delete_segment(segment_id)

    @pytest.mark.API
    def test_can_create_campaign(self, api_client):
        new_campaign_id = api_client.create_campaign()
        api_client.delete_campaign(new_campaign_id)
