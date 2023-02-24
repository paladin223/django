import django.db


# Abstract
class AbstractModel(django.db.models.Model):
    is_published = django.db.models.BooleanField("Публикация", default=True)
    name = django.db.models.CharField("Название", default="", max_length=150)

    class Meta:
        abstract = True
