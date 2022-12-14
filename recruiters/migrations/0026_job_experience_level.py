# Generated by Django 4.1 on 2022-08-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0025_remove_job_banner_job_skills"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="experience_level",
            field=models.CharField(
                choices=[
                    ("Beginner", "Beginner"),
                    ("Intermediate", "Intermediate"),
                    ("Senior", "Senior"),
                ],
                default="Senior",
                max_length=50,
            ),
        ),
    ]
