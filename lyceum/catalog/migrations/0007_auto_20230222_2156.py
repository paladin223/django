# Generated by Django 3.2.16 on 2023-02-22 18:56

import catalog.models

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_auto_20230222_2128"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalogcategory",
            name="slug",
            field=models.CharField(
                default="",
                max_length=150,
                unique=True,
                validators=[catalog.models.slug_validator],
                verbose_name="Ссылка",
            ),
        ),
        migrations.AlterField(
            model_name="catalogitem",
            name="text",
            field=models.TextField(
                default="",
                validators=[catalog.models.text_validator],
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="catalogtag",
            name="slug",
            field=models.CharField(
                default="",
                max_length=150,
                unique=True,
                validators=[catalog.models.slug_validator],
                verbose_name="Ссылка",
            ),
        ),
    ]