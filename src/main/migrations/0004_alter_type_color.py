# Generated by Django 5.1.3 on 2024-11-29 09:14

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_type_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="type",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FFFFFF", image_field=None, max_length=25, samples=None
            ),
        ),
    ]