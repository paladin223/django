# Generated by Django 3.2.16 on 2023-02-22 17:01

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_alter_catalogcategory_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalogcategory",
            name="weight",
            field=models.BigIntegerField(default=100),
        ),
    ]
