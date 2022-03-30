import string
import random
import faker


def fake_phone_number(fake: faker.Faker()) -> str:
    return f'+7-{fake.msisdn()[0:3]}-{fake.msisdn()[0:3]}-{fake.msisdn()[0:2]}-{fake.msisdn()[0:2]}'


def fake_name(fake: faker.Faker()) -> str:
    return fake.name()


def fake_url() -> str:
    return f'https://{"".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))}.com'
