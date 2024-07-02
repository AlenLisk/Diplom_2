from conftest import *
from test_data import *


class TestGetOrders:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_orders_user_with_authorization(self, create_order):
        headers = {'Authorization': create_order}
        response = requests.get(Handles.handle_create_orders, headers=headers)

        assert response.status_code == StatusCode.ok_200 and response.json()['success'] == True and len(
            response.json()['orders']) == 1

    @allure.title('Проверка получения заказов неавторизованного пользователя')
    def test_get_orders_user_without_authorization(self, create_order):
        response = requests.get(Handles.handle_create_orders)

        assert response.status_code == StatusCode.unauthorized_401 and response.json()[
            'success'] == False and ErrorMessage.AUTHORISED in response.text
