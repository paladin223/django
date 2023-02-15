from django.test import Client
from django.test import TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        print(Client().get("/catalog/").json()["name"])
        self.assertEqual(response.status_code, 200)