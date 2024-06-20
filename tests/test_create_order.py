from conftest import *


class TestCreateOrder:
    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_authorization(self, create_user):
        payload = {"ingredients": create_user[2]}
        accessToken = create_user[1]
        headers = {'Authorization': accessToken}
        response = requests.post(Handles.handle_create_orders, headers=headers, json=payload)

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_authorization(self, create_user):
        payload = {"ingredients": create_user[2]}
        response = requests.post(Handles.handle_create_orders, json=payload)

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_user):
        payload = {"ingredients": []}
        accessToken = create_user[1]
        headers = {'Authorization': accessToken}
        response = requests.post(Handles.handle_create_orders, headers=headers, json=payload)

        assert response.status_code == 400 and response.json()[
            'success'] == False and 'Ingredient ids must be provided' in response.text

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_hash_ingredients(self, create_user):
        payload = {"ingredients": ['hashhashhashhash']}
        accessToken = create_user[1]
        headers = {'Authorization': accessToken}
        response = requests.post(Handles.handle_create_orders, headers=headers, json=payload)

        assert response.status_code == 500 and 'Error' in response.text
