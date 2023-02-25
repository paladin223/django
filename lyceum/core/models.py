from django.core import validators
import django.db


# Abstract
class AbstractIsPublished(django.db.models.Model):
    is_published = django.db.models.BooleanField("Публикация", default=True)

    class Meta:
        abstract = True


class AbstractName(django.db.models.Model):
    name = django.db.models.CharField("Название", default="", max_length=150)

    class Meta:
        abstract = True


class AbstractSlug(django.db.models.Model):
    slug = django.db.models.CharField(
        "Ссылка",
        default="",
        max_length=150,
        validators=[
            validators.validate_unicode_slug,
            validators.MaxLengthValidator(200),
        ],
        unique=True,
    )

    class Meta:
        abstract = True


class AbstractStr(django.db.models.Model):
    def __str__(self):
        return self.name

    class Meta:
        abstract = True
