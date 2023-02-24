import catalog.models

from django.contrib import admin


@admin.register(catalog.models.CatalogCategory)
class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.CatalogCategory.id.field.name,
        catalog.models.CatalogCategory.slug.field.name,
        catalog.models.CatalogCategory.weight.field.name,
        catalog.models.CatalogCategory.is_published.field.name,
        catalog.models.CatalogCategory.name.field.name,
    )
    list_editable = (catalog.models.CatalogCategory.is_published.field.name,)
    list_display_links = (catalog.models.CatalogCategory.name.field.name,)


@admin.register(catalog.models.CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.CatalogItem.name.field.name,
        catalog.models.CatalogItem.is_published.field.name,
    )
    list_editable = (catalog.models.CatalogItem.is_published.field.name,)
    list_display_links = (catalog.models.CatalogItem.name.field.name,)
    filter_horizontal = (catalog.models.CatalogItem.tags.field.name,)


@admin.register(catalog.models.CatalogTag)
class CatalogTagAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.CatalogTag.id.field.name,
        catalog.models.CatalogTag.slug.field.name,
        catalog.models.CatalogTag.is_published.field.name,
        catalog.models.CatalogTag.name.field.name,
    )
    list_editable = (catalog.models.CatalogTag.is_published.field.name,)
    list_display_links = (catalog.models.CatalogTag.name.field.name,)
