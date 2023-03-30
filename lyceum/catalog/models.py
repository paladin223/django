from django.core import validators
import django.core.exceptions
import django.db
import django.db.models
import django.template.defaultfilters
import django.utils.safestring
import sorl.thumbnail

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
        default_related_name = "category"


# Tag
class Tag(
    core.models.AbstractSlug,
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"
        default_related_name = "tag"


# Items
class Item(
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    category = django.db.models.ForeignKey(
        "Category",
        on_delete=django.db.models.CASCADE,
        verbose_name="категории",
        default=2,
    )

    text = django.db.models.TextField(
        "Описание",
        default="",
        validators=[catalog.validator.Validator("роскошно", "превосходно")],
    )

    tags = django.db.models.ManyToManyField("Tag", verbose_name="тег")

    @property
    def get_img(self):
        return sorl.thumbnail.get_thumbnail(
            self.mainimage, "300x300", quality=99
        )

    def img_tmb(self):
        if self.mainimage:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_img.url}" />'
            )
        return "картинки нету :("

    img_tmb.short_description = "превью"
    img_tmb.allow_tags = True

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        default_related_name = "item"


class MainImage(core.models.AbstractImage):
    item = django.db.models.OneToOneField(
        Item,
        on_delete=django.db.models.CASCADE,
        blank=True,
    )

    class Meta:
        verbose_name = "Логотип"


class GalleryImage(core.models.AbstractImage):
    item = django.db.models.ForeignKey(
        Item,
        on_delete=django.db.models.CASCADE,
        blank=True,
    )

    class Meta:
        verbose_name = "Фотография галереи"
        verbose_name_plural = "Галерея"
