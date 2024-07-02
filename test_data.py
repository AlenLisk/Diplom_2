class TestData:
    EMAIL = 'non-existent_email'
    PASSWORD = '123456'
    NAME = 'test'
    HASH = 'hashhashhashhash'
    INVALID_PASSWORD = 'invalid_password'
    INVALID_EMAIL = 'invalid_email'

class StatusCode:
    ok_200 = 200
    unauthorized_401 = 401
    forbidden_403 = 403
    bad_request_400 = 400
    internal_server_error_500 = 500

class ErrorMessage:
    USER_ALREADY_EXIST = 'User with such email already exists'
    AUTHORISED = 'You should be authorised'
    INGREDIENT_PROVIDED = 'Ingredient ids must be provided'
    ERROR = 'Error'
    REQUIRED_FIELDS = 'Email, password and name are required fields'
    INCORRECT_FIELDS = 'email or password are incorrect'
