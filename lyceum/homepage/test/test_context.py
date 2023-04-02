from django.core import management
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

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

    def test_home_page_show_correct_context(self):
        response = Client().get(reverse("homepage:home"))
        self.assertIn(
            "items",
            response.context,
            "Items required",
        )
        self.assertNotIn(
            "categories",
            response.context,
            'В контексте присутствует лишний элемент "categories"',
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Главная страница "
            f"возвращает неверный статус {response.status_code}",
        )

    def test_homepage_count_items(self):
        response = Client().get(reverse("homepage:home"))
        items = response.context["items"]
        self.assertEqual(
            items.count(),
            1,
            "На главной странице отображается неверное число товаров",
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Главная страница "
            f"возвращает неверный статус {response.status_code}",
        )

    @parameterized.expand([("name",), ("text",), ("category_id",)])
    def test_homepage_items_contain_positive(self, field):
        response = Client().get(reverse("homepage:home"))
        self.assertIn(
            field,
            list(response.context["items"].values())[0],
            f'В ключах "items" контекста главной страницы '
            f"отсутстует необходимое поле {field}",
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Главная страница "
            f"возвращает неверный статус {response.status_code}",
        )

    @parameterized.expand(
        [("tags",), ("category",), ("items",), ("abcde",), ("280",)]
    )
    def test_homepage_items_contain_negative(self, field):
        response = Client().get(reverse("homepage:home"))
        self.assertNotIn(
            field,
            list(response.context["items"].values())[0],
            f'В ключах "items" контекста главной страницы '
            f"присутстует лишнее поле {field}",
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Главная страница "
            f"возвращает неверный статус {response.status_code}",
        )
