import requests
import json


def test_can_register_user_with_valid_credentials():
    user = {
        "username": "demo1234",
        "password": "123456",
        "email": "demo@gmail.com"
    }
    response = requests.post('http://0.0.0.0/register',
                             data=json.dumps(user),
                             headers={'content-type': 'application/json'})

    assert response.status_code == 200
