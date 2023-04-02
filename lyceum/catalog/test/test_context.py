from django.core import management
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from catalog import models


class ContextTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.published_category = models.Category(
            name="Опубликованная категория", slug="published_category"
        )
        cls.unpublished_category = models.Category(
            name="Неопубликованная категория",
            slug="unpublished_category",
            is_published=False,
        )

        cls.published_tag = models.Tag(
            name="Опубликованный тег", slug="published_tag"
        )
        cls.unpublished_tag = models.Tag(
            name="Неопубликованный тег",
            slug="unpublished_tag",
            is_published=False,
        )

        cls.published_item = models.Item(
            name="Опубликованный товар",
            category=cls.published_category,
            is_on_main=True,
        )
        cls.unpublished_item = models.Item(
            name="Неопубликованный товар",
            category=cls.published_category,
            is_published=False,
            is_on_main=True,
        )

        cls.published_category.clean()
        cls.published_category.save()
        cls.unpublished_category.clean()
        cls.unpublished_category.save()

        cls.published_tag.clean()
        cls.published_tag.save()
        cls.unpublished_tag.clean()
        cls.unpublished_tag.save()

        cls.published_item.clean()
        cls.published_item.save()
        cls.unpublished_item.clean()
        cls.unpublished_item.save()

    @classmethod
    def tearDown(cls):
        management.call_command("flush", verbosity=0, interactive=False)

    def test_catalog_list_context(self):
        response = Client().get(reverse("catalog:main"))
        self.assertIn(
            "items",
            response.context,
            'В контексте присутствует лишний элемент "items"',
        )
        self.assertIn(
            "show_category",
            response.context,
            'В контексте отсутствует обязательный элемент "items"',
        )
        self.assertNotIn(
            "testooo",
            response.context,
            'В контексте отсутствует обязательный элемент "items"',
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Страница каталога "
            f"возвращает неверный статус {response.status_code}",
        )

    def test_catalog_detail_context(self):
        response = Client().get(
            reverse("catalog:item_detail", kwargs={"pk": 1})
        )
        self.assertIn(
            "item",
            response.context,
            'В контексте присутствует лишний элемент "item"',
        )
        self.assertNotIn(
            "items",
            response.context,
            'В контексте отсутствует обязательный элемент "items"',
        )
        self.assertNotIn(
            "categories",
            response.context,
            'В контексте отсутствует обязательный элемент "categories"',
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Страница товара "
            f"возвращает неверный статус {response.status_code}",
        )
