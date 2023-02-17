from http import HTTPStatus

from django.test import Client
from django.test import TestCase


class StaticURLTests(TestCase):
    # common catalog
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_int(self):
        response = Client().get("/catalog/1/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_str(self):
        response = Client().get("/catalog/ooo")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    # re_path test
    def test_catalog_re_int(self):
        response = Client().get("/catalog/re/1/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_multi_int(self):
        response = Client().get("/catalog/re/123/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_multi_negative(self):
        response = Client().get("/catalog/re/-1/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_str(self):
        response = Client().get("/catalog/re/falcon/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_spec(self):
        response = Client().get("/catalog/re/1$/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_float(self):
        response = Client().get("/catalog/re/0.1/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    # regular expression test
    def test_catalog_converter_int(self):
        response = Client().get("/catalog/converter/1/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_multi_int(self):
        response = Client().get("/catalog/converter/123/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_converter_negative(self):
        response = Client().get("/catalog/converter/-1/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_str(self):
        response = Client().get("/catalog/converter/falcon/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_spec(self):
        response = Client().get("/catalog/converter/1$/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_float(self):
        response = Client().get("/catalog/converter/0.1/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)
