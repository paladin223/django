import core.models

import django.core.exceptions
from django.core import validators
import django.db
import django.db.models


def text_validator(value):
    if not ("превосходно" in value) and not ("роскошно" in value):
        raise django.core.exceptions.ValidationError(
            "В тексте должно быть `роскошно` или `превосходно`"
        )


# Category
class Category(core.models.AbstractSlug,
               core.models.AbstractIsPublished,
               core.models.AbstractName,
               core.models.AbstractStr):
    weight = django.db.models.BigIntegerField(
        "Вес",
        default=100,
        validators=[validators.MaxValueValidator(32767), 
                    validators.MinValueValidator(0)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Tag
class Tag(core.models.AbstractSlug,
          core.models.AbstractIsPublished,
          core.models.AbstractName,
          core.models.AbstractStr):

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


# Items
class Item(core.models.AbstractIsPublished,
           core.models.AbstractName,
           core.models.AbstractStr):
    category = django.db.models.ForeignKey(
        "Category",
        on_delete=django.db.models.CASCADE,
        verbose_name="категории",
        related_name="categories",
        default=2,
    )

    text = django.db.models.TextField(
        "Описание",
        default="",
        validators=[text_validator]
    )

    tags = django.db.models.ManyToManyField(
        "Tag",
        verbose_name="тег",
        related_name="items"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
