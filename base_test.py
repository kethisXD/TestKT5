# base_test.py
import requests

class BaseTest:
    BASE_URL = "https://petstore.swagger.io/v2"

    def send_request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response
