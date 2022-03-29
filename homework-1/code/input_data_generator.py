import faker


def fake_phone_number(fake: faker.Faker()) -> str:
    return f'+7-{fake.msisdn()[0:3]}-{fake.msisdn()[0:3]}-{fake.msisdn()[0:2]}-{fake.msisdn()[0:2]}'


def fake_name(fake: faker.Faker()) -> str:
    return fake.name()