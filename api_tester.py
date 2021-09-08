import fire
import requests

API_HOST = "https://cookie-stands-34.herokuapp.com"
RESOURCE_URI = "cookie_stands"
USERNAME = "admin"
PASSWORD = "admin"


class ApiTester:
    """CLI for testing API"""

    def __init__(self, host=API_HOST):
        self.host = host

    def fetch_tokens(self):
        """Fetches access and refresh JWT tokens from api

        Returns:
            tuple: access,refresh
        """

        token_url = f"{self.host}/api/token/"

        response = requests.post(
            token_url, json={"username": USERNAME, "password": PASSWORD}
        )

        data = response.json()

        tokens = data["access"], data["refresh"]

        return tokens

    def get_all(self):
        """get list of all resources from api
        Usage: python api_tester.py get_all

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_one(self, id):
        """get 1 resource by id from api

        Usage:
        python api_tester.py get_one 1

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    # TODO adjust parameter names to match API
    def create(self, location, owner=None, description=None,hourly_sales=None,minimum_customers_per_hour=None,maximum_customers_per_hour=None,average_cookies_per_sale=None):
        """creates a resource in api

        Usage:
        python api_tester.py create /
            --name=required --description=optional --owner=optional

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
            'location':location,
            'owner':owner,
            'description':description,
            'hourly_sales':hourly_sales,
            'minimum_customers_per_hour':minimum_customers_per_hour,
            'maximum_customers_per_hour':maximum_customers_per_hour,
            'average_cookies_per_sale':average_cookies_per_sale,

        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()

    def update(self, location=None, owner=None, description=None,hourly_sales=None,minimum_customers_per_hour=None,maximum_customers_per_hour=None,average_cookies_per_sale=None):
        """updates a resource in api

        Usage:
        python api_tester.py update 1 /
            --name=optional --description=optional --owner=optional

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        original = self.get_cookiestand(id)

        data = {
            'location':location,
            'owner':owner,
            'description':description,
            'hourly_sales':hourly_sales,
            'minimum_customers_per_hour':minimum_customers_per_hour,
            'maximum_customers_per_hour':maximum_customers_per_hour,
            'average_cookies_per_sale':average_cookies_per_sale,

        }

        response = requests.put(url, json=data, headers=headers)

        return response.text

    def delete(self, id):
        """deletes a resource in api

        Usage:
        python api_tester.py delete 1

        Returns: Empty string if no error
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.delete(url, headers=headers)

        return response.text


if __name__ == "__main__":
    fire.Fire(ApiTester)
