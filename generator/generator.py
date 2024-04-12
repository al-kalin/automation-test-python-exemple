import random

from data.data import Person, Color, Date

from faker import Faker

faker_ua = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ua.first_name() + " " + faker_ua.last_name() + " " + faker_ua.middle_name(),
        first_name=faker_ua.first_name(),
        last_name=faker_ua.last_name(),
        age=random.randint(10, 80),
        department=faker_ua.job(),
        salary=random.randint(1000, 20000),
        email=faker_ua.email(),
        current_address=faker_ua.address(),
        permanent_address=faker_ua.address(),
        mobile=faker_ua.msisdn(),
    )


def generated_file():
    path = f'/Users/alkalin/al_kalin/auto tests/automation-test-python-example/filetest_{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00",
    )
