# Generated by Django 3.2.16 on 2023-02-22 16:59

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_auto_20230222_1958"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalogcategory",
            name="weight",
            field=models.BigIntegerField(default=0),
        ),
    ]
