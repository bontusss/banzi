# Generated by Django 4.1 on 2022-08-31 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0011_remove_profile_is_candidate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="facebook_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="github_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="linkedin_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="twitter_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]