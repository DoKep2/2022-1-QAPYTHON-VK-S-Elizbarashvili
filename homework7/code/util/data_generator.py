import string
import random
import faker


class DataGenerator:

    @staticmethod
    def fake_phone_number() -> str:
        return f'+7-{faker.Faker().msisdn()[0:3]}-{faker.Faker().msisdn()[0:3]}-{faker.Faker.msisdn()[0:2]}-{faker.Faker().msisdn()[0:2]}'

    @staticmethod
    def fake_name() -> str:
        return faker.Faker().name().split()[0]

    @staticmethod
    def fake_url() -> str:
        return f'https://{"".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))}.com'

    @staticmethod
    def fake_number() -> str:
        return str(random.randint(0, 100))
