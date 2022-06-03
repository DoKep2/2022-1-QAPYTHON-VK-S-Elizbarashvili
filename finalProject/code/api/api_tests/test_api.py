import allure
import pytest

from conftest import MySql
from data_generator import MyFaker

faker = MyFaker()


class TestClass(MySql):
    @allure.epic('API tests')
    @allure.title('Correct user login')
    def test_login(self, api_client):
        res = api_client.post_login()
        assert res.url == 'http://app:8089/welcome/'

    @allure.epic('API tests')
    @allure.title('Incorrect user login')
    @pytest.mark.xfail
    @pytest.mark.parametrize('username, password', [("invalidUsername", "invalidPassword")])
    def test_invalid_username_login_bug(self, api_client, username, password):
        res = api_client.invalid_login(username, password)
        assert res.status_code == 404

    @allure.epic('API tests')
    @allure.title('User login with invalid password')
    @pytest.mark.xfail
    @pytest.mark.parametrize('password', ["invalidPassword"])
    def test_invalid_password_login(self, api_client, password):
        res = api_client.invalid_login("DoKepDoKep", password)
        assert res.status_code == 404

    @allure.epic('API tests')
    @allure.title('Add user')
    @pytest.mark.xfail
    def test_add_user(self, api_client):
        user_data = faker.fake_valid_user_data()
        username = user_data['username']
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_before == 0
        res = api_client.add_user(user_data)
        assert res.status_code == 201
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_after == 1

    @allure.epic('API tests')
    @allure.title('Add user without middlename')
    @pytest.mark.xfail
    def test_add_user_without_middlename(self, api_client):
        user_data = faker.fake_valid_user_data()
        user_data['middle_name'] = None
        username = user_data['username']
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_before == 0
        res = api_client.add_user(user_data)
        assert res.status_code == 201
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_after == 1

    @allure.epic('API tests')
    @allure.title('Add user with too long name')
    @pytest.mark.xfail
    def test_add_user_with_too_long_name_bug(self, api_client):
        user_data = api_client.fake_invalid_user_data(name=MyFaker.fake_too_long_name())
        username = user_data['username']
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_before == 0
        res = api_client.add_user(user_data)
        assert res.status_code == 400
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_after == 0

    @allure.epic('API tests')
    @allure.title('Add user with too long email')
    @pytest.mark.xfail
    def test_add_user_with_too_long_email(self, api_client):
        user_data = api_client.fake_invalid_user_data(email=MyFaker.fake_too_long_email())
        username = user_data['username']
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_before == 0
        res = api_client.add_user(user_data)
        assert res.status_code == 400
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_after == 0

    @allure.epic('API tests')
    @allure.title('Add user with too long password')
    @pytest.mark.xfail
    def test_add_user_with_too_long_password(self, api_client):
        user_data = api_client.fake_invalid_user_data(password=MyFaker.fake_too_long_name())
        username = user_data['username']
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_before == 0
        res = api_client.add_user(user_data)
        assert res.status_code == 400
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_after == 0

    @allure.epic('API tests')
    @allure.title('Delete user')
    def test_delete_user(self, api_client):
        user_data = faker.fake_valid_user_data()
        username = user_data['username']
        api_client.add_user(user_data)
        users_count_with_correspondent_name_before = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_before == 1
        res = api_client.delete_user(user_data['username'])
        assert res.status_code == 204
        users_count_with_correspondent_name_after = len(self.client.get_users_by_username(username))
        assert users_count_with_correspondent_name_after == 0

    @allure.epic('API tests')
    @allure.title('Change user password')
    @pytest.mark.xfail
    def test_change_password_bug(self, api_client):
        user_data = faker.fake_valid_user_data()
        username = user_data['username']
        api_client.add_user(user_data)
        new_password = MyFaker.fake_name()
        res = api_client.change_password(user_data['username'], new_password)
        correspondent_user = self.client.get_users_by_username(username)[0]
        assert correspondent_user.password == new_password
        assert res.status_code == 200 # expc 204

    @allure.epic('API tests')
    @allure.title('Block user')
    def test_block_user(self, api_client):
        user_data = faker.fake_valid_user_data()
        username = user_data['username']
        api_client.add_user(user_data)
        user_access_before = self.client.get_users_by_username(username)[0].access
        assert user_access_before == 1
        res = api_client.block_user(user_data['username'])
        assert res.status_code == 200
        assert res.json()['detail'] == 'User was blocked'
        user_access_after = self.client.get_users_by_username(username)[0].access
        assert user_access_after == 0

    @allure.epic('API tests')
    @allure.title('Accept user')
    def test_accept_user(self, api_client):
        user_data = faker.fake_valid_user_data()
        username = user_data['username']
        api_client.add_user(user_data)
        api_client.block_user(user_data['username'])
        res = api_client.accept_user(user_data['username'])
        assert res.json()['detail'] == 'User access granted'
        assert res.status_code == 200
        user_access_after = self.client.get_users_by_username(username)[0].access
        assert user_access_after == 1

    @allure.epic('API tests')
    @allure.title('Get status')
    def test_get_status(self, api_client):
        res = api_client.get_status()
        assert res.status_code == 200
        assert res.json()['status'] == 'ok'
