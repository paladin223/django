import django.db


class AbstractModel(django.db.models.Model):
    class Meta:
        abstract = True


class CatalogCategory(AbstractModel):
    pass


class CatalogItem(AbstractModel):
    pass


class CatalogTag(AbstractModel):
    pass