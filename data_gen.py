import random
import string
from datetime import datetime, timedelta
class DataGeneration:
    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def register_new_user_and_return_login_password(self, length=10):

        email= f'{self.generate_random_string(length)}@gmail.com'
        password = self.generate_random_string(length)
        name = self.generate_random_string(length)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload
