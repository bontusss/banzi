# Generated by Django 4.1 on 2022-08-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0028_job_category_job_company_job_type"),
        ("candidates", "0008_alter_profile_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="skills",
            field=models.ManyToManyField(to="recruiters.skill"),
        ),
    ]
