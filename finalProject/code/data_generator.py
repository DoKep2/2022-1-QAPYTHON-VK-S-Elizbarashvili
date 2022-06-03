import pdb
import random
import string

import faker


class MyFaker:

    @classmethod
    def fake_phone_number(cls) -> str:
        return f'+7-{faker.Faker().msisdn()[0:3]}-{faker.Faker().msisdn()[0:3]}-{faker.Faker.msisdn()[0:2]}-{faker.Faker().msisdn()[0:2]}'

    @classmethod
    def fake_name(cls) -> str:
        return faker.Faker().name()

    @classmethod
    def fake_url(cls) -> str:
        return f'https://{"".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))}.com'

    @classmethod
    def fake_email(cls) -> str:
        return faker.Faker().email()

    @classmethod
    def fake_valid_name(cls):
        return faker.Faker().name()[:255]

    @classmethod
    def fake_too_long_name(cls):
        return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(256))

    @classmethod
    def fake_too_short_name(cls):
        return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    @classmethod
    def fake_valid_username(cls):
        return cls.fake_name()[:16]

    @classmethod
    def fake_too_long_username(cls):
        return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))

    @classmethod
    def fake_too_short_username(cls):
        return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    @classmethod
    def fake_valid_email(cls):
        return cls.fake_email()[:64]

    @classmethod
    def fake_too_long_email(cls):
        return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(57)) + "@mail.ru"

    @classmethod
    def fake_too_short_email(cls):
        return "".join(random.choice(string.ascii_uppercase + string.digits)) + "@a.r"

    @classmethod
    def fake_valid_user_data(cls) -> dict:
        return {
            "name": cls.fake_valid_name(),
            "surname": cls.fake_valid_name(),
            "middle_name": cls.fake_valid_name(),
            "username": cls.fake_valid_username(),
            "password": cls.fake_valid_name(),
            "email": cls.fake_valid_email(),
        }
