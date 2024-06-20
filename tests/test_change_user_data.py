from conftest import *


class TestChangeUserData:
    @allure.title('Проверка изменения имени авторизованного пользователя')
    def test_change_user_name_with_authorization(self, create_user):
        payload = create_user[0]
        payload['name'] = 'test'
        accessToken = create_user[1]
        headers = {'Authorization': accessToken}
        response = requests.patch(Handles.handle_change_user_data, headers=headers, data=payload)

        assert response.status_code == 200 and response.json()['success'] == True and response.json()['user'][
            'name'] == 'test'

    @allure.title('Проверка изменеия email авторизованного пользователя')
    def test_change_user_email_with_authorization(self, create_user):
        payload = create_user[0]
        payload['email'] = f'{DataGeneration.generate_random_string()}@gmail.com'
        accessToken = create_user[1]
        headers = {'Authorization': accessToken}
        response = requests.patch(Handles.handle_change_user_data, headers=headers, data=payload)

        assert response.status_code == 200 and response.json()['success'] == True and response.json()['user'][
            'email'] == payload['email']

    @allure.title('Проверка изменеия пароля авторизованного пользователя')
    def test_change_user_password_with_authorization(self, create_user):
        payload = create_user[0]
        payload['password'] = '123456'
        accessToken = create_user[1]
        headers = {'Authorization': accessToken}
        response = requests.patch(Handles.handle_change_user_data, headers=headers, data=payload)

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка изменеия email авторизованного пользователя на уже используемый')
    def test_change_user_email_with_authorization_exists_email(self, create_payload, create_user):
        payload_1 = create_user[0]
        del payload_1['password']
        accessToken = create_user[1]

        data_generation = DataGeneration()
        payload_2 = data_generation.register_new_user_and_return_login_password()
        requests.post(Handles.handle_create_user, data=payload_2)
        payload_1['email'] = payload_2['email']

        headers = {'Authorization': accessToken}
        response = requests.patch(Handles.handle_change_user_data, headers=headers, data=payload_1)

        assert response.status_code == 403 and response.json()[
            'success'] == False and 'User with such email already exists' in response.text

    @allure.title('Проверка изменения имени неавторизованного пользователя')
    def test_change_user_name_without_authorization(self, create_user):
        payload = create_user[0]
        payload['name'] = 'test'
        response = requests.patch(Handles.handle_change_user_data, data=payload)

        assert response.status_code == 401 and response.json()[
            'success'] == False and 'You should be authorised' in response.text

    @allure.title('Проверка изменеия email неавторизованного пользователя')
    def test_change_user_email_without_authorization(self, create_user):
        payload = create_user[0]
        payload['email'] = f'{DataGeneration.generate_random_string()}@gmail.com'
        response = requests.patch(Handles.handle_change_user_data, data=payload)

        assert response.status_code == 401 and response.json()[
            'success'] == False and 'You should be authorised' in response.text

    @allure.title('Проверка изменеия пароля неавторизованного пользователя')
    def test_change_user_password_without_authorization(self, create_user):
        payload = create_user[0]
        payload['password'] = '123456'
        response = requests.patch(Handles.handle_change_user_data, data=payload)

        assert response.status_code == 401 and response.json()[
            'success'] == False and 'You should be authorised' in response.text
