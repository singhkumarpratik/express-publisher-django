# Generated by Django 3.0.5 on 2020-04-26 22:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_express_publish_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='express_publish',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
