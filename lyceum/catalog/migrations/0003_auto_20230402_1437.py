# Generated by Django 3.2.16 on 2023-04-02 11:37

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_item_is_on_main"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galleryimage",
            name="item",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="catalog.item",
            ),
        ),
        migrations.AlterField(
            model_name="mainimage",
            name="item",
            field=models.OneToOneField(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mainimage",
                to="catalog.item",
            ),
        ),
    ]
