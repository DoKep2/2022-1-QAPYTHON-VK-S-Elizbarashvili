import pytest

from api.api_client.client import ApiClient


@pytest.fixture(scope="function")
def api_client():
    LOGIN = "DoKepDoKep"
    PASSWORD = "DoKepDoKep"
    URL = "http://app:8089/login"
    api_client = ApiClient(URL, LOGIN, PASSWORD)
    api_client.post_login()
    return api_client
