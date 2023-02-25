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


# @deconstructible
# class text_validator:
#     def __init__(self, *kwargs):
#         self.words = kwargs
    
#     def __call__(self, value):
#         for value in self.words:
#             if value in self.words:
#                 return True
    
#         raise django.core.exceptions.ValidationError(
#             "В тексте должно быть `роскошно` или `превосходно`")


# Category
class Category(core.models.AbstractModelCatalog):
    slug = django.db.models.CharField(
        "Ссылка",
        default="",
        max_length=150,
        validators=[validators.validate_unicode_slug,
                    validators.MaxLengthValidator(200)],
        unique=True,
    )
    weight = django.db.models.BigIntegerField(
        "Вес",
        default=100,
        validators=[validators.MaxValueValidator(32767), 
                    validators.MinValueValidator(0)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name


# Tag
class Tag(core.models.AbstractModelCatalog):
    slug = django.db.models.CharField(
        "Ссылка",
        default="",
        max_length=150,
        validators=[validators.validate_unicode_slug,
                    validators.MaxLengthValidator(200)],
        unique=True,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


# Items
class Item(core.models.AbstractModelCatalog):
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
    
    def __str__(self):
        return self.name
