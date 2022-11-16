# Generated by Django 4.1 on 2022-08-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_alter_apijobs_created_alter_apijobs_job_level_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                (
                    "name",
                    models.CharField(
                        help_text="Name of the reviewer", max_length=100, null=True
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Eg. Product Manager", max_length=50, null=True
                    ),
                ),
                ("review", models.TextField(null=True)),
            ],
        ),
    ]