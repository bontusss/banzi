# Generated by Django 4.1 on 2022-08-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0015_job_deadline"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="full_address",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
