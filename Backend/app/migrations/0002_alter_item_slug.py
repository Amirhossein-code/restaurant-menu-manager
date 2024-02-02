# Generated by Django 5.0.1 on 2024-02-02 19:07

import autoslug.fields
import common.utils.custom_slug_utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='title', slugify=common.utils.custom_slug_utils.custom_slugify, unique=True),
        ),
    ]
