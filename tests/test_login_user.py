from conftest import *
from test_data import *


class TestLoginCourier:
    @allure.title('Проверка логина пользователя')
    def test_courier_login(self, create_user):
        payload = create_user[0]
        del payload['name']
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == StatusCode.ok_200 and response_login.json()['success'] == True

    @allure.title('Проверка логина без email')
    def test_courier_login_without_email(self, create_user):
        payload = create_user[0]
        del payload['name']
        payload['email'] = ''
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == StatusCode.unauthorized_401 and ErrorMessage.INCORRECT_FIELDS in response_login.text

    @allure.title('Проверка логина без пароля')
    def test_courier_login_without_password(self, create_user):
        payload = create_user[0]
        del payload['name']
        payload['password'] = ''
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == StatusCode.unauthorized_401 and ErrorMessage.INCORRECT_FIELDS in response_login.text

    @allure.title('Проверка логина с невалидным email')
    def test_courier_login_with_invalid_email(self, create_payload):
        payload = create_payload
        payload['email'] = TestData.INVALID_EMAIL
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == StatusCode.unauthorized_401 and ErrorMessage.INCORRECT_FIELDS in response_login.text

    @allure.title('Проверка логина с невалидным паролем')
    def test_courier_login_with_invalid_password(self, create_payload):
        payload = create_payload
        payload['password'] = TestData.INVALID_PASSWORD
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == StatusCode.unauthorized_401 and ErrorMessage.INCORRECT_FIELDS in response_login.text

    @allure.title('Проверка логина с несуществующим пользователем')
    def test_unregistered_user_login(self):
        payload = {}
        payload['email'] = TestData.EMAIL
        payload['password'] = TestData.PASSWORD
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == StatusCode.unauthorized_401 and ErrorMessage.INCORRECT_FIELDS in response_login.text
