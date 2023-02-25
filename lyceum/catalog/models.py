import core.models

import django.core.exceptions
from django.core import validators
import django.db
import django.db.models
from django.utils.deconstruct import deconstructible


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


def slug_validator(value):
    # len validator
    if len(value) > 200:
        raise django.core.exceptions.ValidationError("Максимальная длина 200!")

    # text validator
    verbs = ""

    verbs = "".join([chr(i) for i in range(ord("a"), ord("a") + 26)])  # a-z
    verbs += "".join([str(i) for i in range(10)])  # 0 - 9
    verbs += "-_"  # -_
    verbs = set(verbs)
    if len(set(value).difference(verbs)) > 0:
        raise django.core.exceptions.ValidationError(
            "В тексте должны быть только цифры,"
            "буквы латиницы и символы - и _"
        )


def weight_validator(value):
    if not (value in range(0, 32768)):
        raise django.core.exceptions.ValidationError(
            "Число в промежтке от" "(0 - 32767)!"
        )


# Category
class CatalogCategory(core.models.AbstractModel):
    slug = django.db.models.CharField(
        "Ссылка",
        default="",
        max_length=150,
        validators=[slug_validator],
        unique=True,
    )
    weight = django.db.models.BigIntegerField("Вес", default=100,
                                              validators=[weight_validator])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name[:200]


# Tag
class CatalogTag(core.models.AbstractModel):
    slug = django.db.models.CharField(
        "Ссылка",
        default="",
        max_length=150,
        validators=[slug_validator],
        unique=True,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name[:200]


# Items
class CatalogItem(core.models.AbstractModel):
    text = django.db.models.TextField(
        "Описание", default="", validators=[text_validator("роскошно", "превосходно")]
    )

    tags = django.db.models.ManyToManyField(
        CatalogTag, verbose_name="тег", related_name="items"
    )

    category = django.db.models.ForeignKey(
        "CatalogCategory",
        on_delete=django.db.models.CASCADE,
        verbose_name="категории",
        related_name="catalog_categories",
        default=2,
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:200]
