# Generated by Django 4.1 on 2022-08-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0002_category_job_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="popular",
            field=models.BooleanField(default=False),
        ),
    ]