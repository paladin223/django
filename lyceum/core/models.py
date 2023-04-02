import django.db
import django.utils.safestring
import sorl.thumbnail


# Abstract
class AbstractIsPublished(django.db.models.Model):
    is_published = django.db.models.BooleanField("публикация", default=True)

    class Meta:
        abstract = True


class AbstractName(django.db.models.Model):
    name = django.db.models.CharField(
        "название", default="", unique=True, max_length=150
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractSlug(django.db.models.Model):
    slug = django.db.models.SlugField(
        "слаг",
        default="",
        max_length=200,
        unique=True,
    )

    class Meta:
        abstract = True


class AbstractImage(django.db.models.Model):
    upload = django.db.models.ImageField(
        "фото",
        upload_to="uploads",
    )

    @property
    def get_img(self):
        return sorl.thumbnail.get_thumbnail(self.upload, "50x50", quality=99)

    def image_tmb(self):
        if self.upload:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_img.url}" />'
            )
        return "картинки нету :("

    @property
    def image_cropped(self):
        return sorl.thumbnail.get_thumbnail(
            self.upload, "1000x1000", crop="center"
        )

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    def __str__(self):
        return self.upload.name

    class Meta:
        abstract = True
