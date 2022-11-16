# Generated by Django 4.1 on 2022-08-25 09:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0009_category_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default="test", editable=False, populate_from="name", unique=True
            ),
            preserve_default=False,
        ),
    ]
