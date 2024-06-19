import pytest
from data_gen import DataGeneration
import allure
from handles import Handles
import requests

@pytest.fixture
def create_payload():
    data_generation = DataGeneration()
    payload = data_generation.register_new_user_and_return_login_password()

    return payload

@pytest.fixture
def create_user(create_payload):
    payload = create_payload
    response = requests.post(Handles.handle_create_user, data=payload)
    del payload['name']

    accessToken = response.json()['accessToken']
    refreshToken = response.json()['refreshToken']

    return payload, accessToken, refreshToken
