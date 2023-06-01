from scr.conditions import status_code, body
from scr.services import UserApiService
from hamcrest import has_length, greater_than
from faker import Faker


def test_can_register_user_with_valid_credentials(faker: Faker) -> None:
    user: dict[str, str] = {
        "username": faker.name(),
        "password": "123456",
        "email": "demo@gmail.com"
    }
    response = UserApiService().create_user(user)

    response.should_have(status_code(200))
    response.should_have(body('$.id', has_length(greater_than(0))))


def test_can_not_register_user_with_same_credentials_twice(faker: Faker) -> None:
    user: dict[str, str] = {
        "username": faker.name(),
        "password": "123456",
        "email": "demo@gmail.com"
    }
    response = UserApiService().create_user(user)

    response.should_have(status_code(200))

    response = UserApiService().create_user(user)

    response.should_have(status_code(500))
