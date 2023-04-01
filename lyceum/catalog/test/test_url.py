from http import HTTPStatus

import django.core.exceptions
import django.test
import parameterized


class StaticURLTests(django.test.TestCase):
    # common catalog
    def test_catalog_endpoint(self):
        response = django.test.Client().get("/catalog/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_str(self):
        response = django.test.Client().get("/catalog/ooo/")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    # re_path test
    @parameterized.parameterized.expand(
        [
            ("-1", HTTPStatus.NOT_FOUND),
            ("0.1", HTTPStatus.NOT_FOUND),
            ("010", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_re_nums_bad(self, value, expected):
        response = django.test.Client().get(f"/catalog/re/{value}/")
        self.assertEqual(response.status_code, expected)

    def test_catalog_re_int(self):
        response = django.test.Client().get("/catalog/re/1/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_multi_int(self):
        response = django.test.Client().get("/catalog/re/123/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_str(self):
        response = django.test.Client().get("/catalog/re/falcon/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_spec(self):
        response = django.test.Client().get("/catalog/re/1$/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    # regular expression test
    @parameterized.parameterized.expand(
        [
            ("-1", HTTPStatus.NOT_FOUND),
            ("0.1", HTTPStatus.NOT_FOUND),
            ("010", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_converter_nums_bad(self, value, expected):
        response = django.test.Client().get(f"/catalog/re/{value}/")
        self.assertEqual(response.status_code, expected)

    def test_catalog_converter_int(self):
        response = django.test.Client().get("/catalog/converter/1/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_multi_int(self):
        response = django.test.Client().get("/catalog/converter/123/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_str(self):
        response = django.test.Client().get("/catalog/converter/falcon/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter_spec(self):
        response = django.test.Client().get("/catalog/converter/1$/")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)
