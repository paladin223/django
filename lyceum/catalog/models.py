from django.core import validators
import django.core.exceptions
import django.db
import django.db.models

import catalog.validator
import core.models


# Category
class Category(
    core.models.AbstractSlug,
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    weight = django.db.models.BigIntegerField(
        "вес",
        default=100,
        validators=[
            validators.MaxValueValidator(32767),
            validators.MinValueValidator(0),
        ],
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


# Tag
class Tag(
    core.models.AbstractSlug,
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


# Items
class Item(
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    category = django.db.models.ForeignKey(
        "Category",
        on_delete=django.db.models.CASCADE,
        verbose_name="категории",
        related_name="category",
        default=2,
    )

    text = django.db.models.TextField(
        "Описание",
        default="",
        validators=[
            catalog.validator.Validator(
                "роскошно", "классно", "замечательно", "превосходно"
            )
        ],
    )

    tags = django.db.models.ManyToManyField(
        "Tag", verbose_name="тег", related_name="tag"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
