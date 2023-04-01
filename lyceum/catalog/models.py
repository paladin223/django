from django.core import validators
import django.core.exceptions
import django.db.models
import django.template.defaultfilters
import django.utils.safestring
import sorl.thumbnail

import catalog.validator
import core.models


class CategoryManager(django.db.models.Manager):
    def published(self):
        return self.get_queryset().filter(is_published=True)


# Category
class Category(
    core.models.AbstractSlug,
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    objects = CategoryManager()
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


class TagManager(django.db.models.Manager):
    def published(self):
        return self.get_queryset().filter(is_published=True)


# Tag
class Tag(
    core.models.AbstractSlug,
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    objects = TagManager()

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"
        default_related_name = "tag"


class ItemManager(django.db.models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .select_related(
                Category._meta.model_name,
                "mainimage",
            )
            .prefetch_related(
                django.db.models.Prefetch(
                    Item.tags.field.name,
                    queryset=Tag.objects.published().only(Tag.name.field.name),
                )
            )
            .only(
                Item.name.field.name,
                Item.text.field.name,
                f"{Item.category.field.name}__{Category.name.field.name}",
                Item.tags.field.name,
                Item._meta.get_field("mainimage").name,
            )
        )


# Items
class Item(
    core.models.AbstractIsPublished,
    core.models.AbstractName,
):
    objects = ItemManager()
    category = django.db.models.ForeignKey(
        "Category",
        on_delete=django.db.models.CASCADE,
        verbose_name="категории",
        default=2,
    )

    is_on_main = django.db.models.BooleanField(
        "показывается на главной", default=False
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
            self.mainimage, "300x300", crop="center"
        )

    @property
    def img_catalog(self):
        return sorl.thumbnail.get_thumbnail(
            self.mainimage, "150x100", crop="center"
        )

    @property
    def img_detail(self):
        return sorl.thumbnail.get_thumbnail(
            self.mainimage, "500x500", crop="center"
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
        related_name="mainimage",
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
