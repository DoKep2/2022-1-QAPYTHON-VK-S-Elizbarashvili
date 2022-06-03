from mysql.sql_models.models import UserModel


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def add_user(self, name, surname, username, email, password, middle_name):
        user = UserModel(
            name=name,
            surname=surname,
            username=username,
            email=email,
            password=password,
            middle_name=middle_name,
        )
        self.client.session.add(user)
        self.client.session.commit()

