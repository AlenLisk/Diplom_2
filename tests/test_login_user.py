from conftest import *


class TestLoginCourier:
    @allure.title('Проверка логина пользователя')
    def test_courier_login(self, create_user):
        payload = create_user[0]
        del payload['name']
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == 200 and response_login.json()['success'] == True

    @allure.title('Проверка логина без email')
    def test_courier_login_without_email(self, create_user):
        payload = create_user[0]
        del payload['name']
        payload['email'] = ''
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == 401 and 'email or password are incorrect' in response_login.text

    @allure.title('Проверка логина без пароля')
    def test_courier_login_without_password(self, create_user):
        payload = create_user[0]
        del payload['name']
        payload['password'] = ''
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == 401 and 'email or password are incorrect' in response_login.text

    @allure.title('Проверка логина с невалидным email')
    def test_courier_login_with_invalid_email(self, create_payload):
        payload = create_payload
        payload['email'] = 'invalid_email'
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == 401 and 'email or password are incorrect' in response_login.text

    @allure.title('Проверка логина с невалидным паролем')
    def test_courier_login_with_invalid_password(self, create_payload):
        payload = create_payload
        payload['password'] = 'invalid_password'
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == 401 and 'email or password are incorrect' in response_login.text

    @allure.title('Проверка логина с несуществующим пользователем')
    def test_unregistered_user_login(self):
        payload = {}
        payload['email'] = 'non-existent_email'
        payload['password'] = '1234'
        response_login = requests.post(Handles.handle_login_user, data=payload)

        assert response_login.status_code == 401 and 'email or password are incorrect' in response_login.text
