from django.test import Client
from django.test import TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)
