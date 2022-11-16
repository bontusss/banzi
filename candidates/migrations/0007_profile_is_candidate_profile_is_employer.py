# Generated by Django 4.1 on 2022-08-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0006_appliedjobs_profile_savedjobs_delete_candidate"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_candidate",
            field=models.BooleanField(
                default=True,
                help_text="Check this if you are looking for a job.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_employer",
            field=models.BooleanField(
                default=False, help_text="Check this if you are an employer.", null=True
            ),
        ),
    ]
