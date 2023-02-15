from django.test import Client
from django.test import TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_int(self):
        response = Client().get("/catalog/1")
        self.assertEqual(response.status_code, 200)

    def test_catalog_str(self):
        response = Client().get("/catalog/ooo")
        self.assertNotEqual(response.status_code, 200)
