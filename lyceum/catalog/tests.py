from http import HTTPStatus
import unittest

import catalog.models
import parameterized

import django.core.exceptions
import django.test


class StaticURLTests(django.test.TestCase):
    # common catalog
    def test_catalog_endpoint(self):
        response = django.test.Client().get("/catalog/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_int(self):
        response = django.test.Client().get("/catalog/1/")
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


class ModelsTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="test category",
            slug="test-category-slug",
            weight=100,
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="test category",
            slug="test-category-slug",
        )

    @classmethod
    def tearDownClass(cls):
        cls.category = catalog.models.Category.objects.all().delete()
        cls.item = catalog.models.Item.objects.all().delete()
        cls.tag = catalog.models.Tag.objects.all().delete()
        super().tearDownClass()

    def test_unable_create_without_great_in_text(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name="test item",
                category=self.category,
                text="невероятный",
                is_published=True,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )

    @parameterized.parameterized.expand([("превосходно"), ("роскошно")])
    def test_good_catalog_item(self, value):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            name="item",
            category=self.category,
            text=value,
            is_published=True,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTest.tag)

        self.assertNotEqual(catalog.models.Item.objects.count(), item_count)

    def test_zero_vals_catalog_item(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item()
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )

    def test_bad_slug_catalog_tag(self):
        tag_count = catalog.models.Tag.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Tag(
                name="tag",
                slug="probel -i_tekst",
                is_published=True,
            )
            self.item.full_clean()
            self.item.save()

        self.assertEqual(
            catalog.models.Tag.objects.count(),
            tag_count,
        )

    def test_good_slug_catalog_tag(self):
        tag_count = catalog.models.Tag.objects.count()
        self.item = catalog.models.Tag(
            name="tag",
            slug="probel-i_tekst",
            is_published=True,
        )
        self.item.full_clean()
        self.item.save()

        self.assertNotEqual(
            catalog.models.Tag.objects.count(),
            tag_count,
        )

    @parameterized.parameterized.expand(
        [
            ("bad",),
            (-1,),
            (1000000000,),
        ]
    )
    def test_bad_catalog_category_weight(self, value):
        category_count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Category(
                name="tag",
                is_published=True,
                slug="word-owl",
                weight=value,
            )
            self.item.full_clean()
            self.item.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            category_count,
        )

    @parameterized.parameterized.expand(
        [
            (0,),
            (100,),
            (32767,),
            (1,),
        ]
    )
    def test_good_catalog_category_weight(self, value):
        category_count = catalog.models.Category.objects.count()
        self.item = catalog.models.Category(
            name="tag",
            is_published=True,
            slug="word-owl",
            weight=value,
        )
        self.item.full_clean()
        self.item.save()

        self.assertNotEqual(
            catalog.models.Category.objects.count(),
            category_count,
        )
