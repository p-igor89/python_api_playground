from scr.services import UserApiService


def test_can_register_user_with_valid_credentials(faker):
    user = {
        "username": faker.name(),
        "password": "123456",
        "email": "demo@gmail.com"
    }
    response = UserApiService.create_user(user)

    assert response.status_code == 200


def test_can_not_register_user_with_same_credentials_twice(faker):
    user = {
        "username": faker.name(),
        "password": "123456",
        "email": "demo@gmail.com"
    }
    response = UserApiService.create_user(user)

    assert response.status_code == 200

    response = UserApiService.create_user(user)

    assert response.status_code == 500
