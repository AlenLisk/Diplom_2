from conftest import *


class TestCreateUser:
    @allure.title('Проверка создания пользователя')
    def test_create_user(self, create_payload):
        payload = create_payload
        response = requests.post(Handles.handle_create_user, data=payload)

        assert response.status_code == 200 and response.json()['user']['email'] == payload['email']

    @allure.title('Проверка создания зарегистрированного пользователя')
    def test_create_two_identical_users(self, create_payload):
        payload = create_payload
        requests.post(Handles.handle_create_user, data=payload)
        response_conflict = requests.post(Handles.handle_create_user, data=payload)

        assert response_conflict.status_code == 403 and 'User already exists"' in response_conflict.text

    @allure.title('Проверка регистрации пользователя без имени')
    def test_create_user_without_name(self, create_payload):
        payload = create_payload
        payload['name'] = ''
        response_create = requests.post(Handles.handle_create_user, data=payload)

        assert response_create.status_code == 403 and 'Email, password and name are required fields' in response_create.text

    @allure.title('Проверка регистрации пользователя без email')
    def test_create_user_without_email(self, create_payload):
        payload = create_payload
        payload['email'] = ''
        response_create = requests.post(Handles.handle_create_user, data=payload)

        assert response_create.status_code == 403 and 'Email, password and name are required fields' in response_create.text

    @allure.title('Проверка регистрации пользователя без пароля')
    def test_create_user_without_password(self, create_payload):
        payload = create_payload
        payload['password'] = ''
        response_create = requests.post(Handles.handle_create_user, data=payload)

        assert response_create.status_code == 403 and 'Email, password and name are required fields' in response_create.text