# Generated by Django 4.1 on 2022-08-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0007_alter_category_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
