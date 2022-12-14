# Generated by Django 4.1 on 2022-08-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="APIJOBS",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, null=True)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("slug", models.SlugField()),
                ("description", models.TextField()),
                ("url", models.URLField()),
                ("location", models.CharField(max_length=100)),
                ("job_type", models.CharField(max_length=50)),
                ("job_level", models.CharField(max_length=100)),
                ("created", models.DateTimeField()),
            ],
        ),
    ]
