# Generated by Django 4.1 on 2022-08-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0016_job_full_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="country",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="state",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
