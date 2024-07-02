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

    accessToken = response.json()['accessToken']
    response = requests.get(Handles.handle_get_ingredients, headers={'Authorization': accessToken})
    ingredients_list = []
    ingredients_list.append(response.json()['data'][1]['_id'])

    return payload, accessToken, ingredients_list


@pytest.fixture
def create_order(create_user):
    payload = {"ingredients": create_user[2]}
    accessToken = create_user[1]
    headers = {'Authorization': accessToken}
    requests.post(Handles.handle_create_orders, headers=headers, json=payload)

    return accessToken
