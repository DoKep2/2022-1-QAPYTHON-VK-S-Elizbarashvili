import pytest


@pytest.fixture(scope="function")
def api_client():
    LOGIN = "esmbot@yandex.ru"
    PASSWORD = "36hrzUCPJj-&T2."
    URL = "https://target.my.com/csrf/"
    from api.client import ApiClient
    api_client = ApiClient(URL, LOGIN, PASSWORD)
    api_client.post_login()
    return api_client
