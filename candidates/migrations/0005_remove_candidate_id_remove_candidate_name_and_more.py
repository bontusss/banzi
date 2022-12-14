# Generated by Django 4.1 on 2022-08-25 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("candidates", "0004_candidate_top"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidate",
            name="id",
        ),
        migrations.RemoveField(
            model_name="candidate",
            name="name",
        ),
        migrations.RemoveField(
            model_name="candidate",
            name="photo",
        ),
        migrations.RemoveField(
            model_name="candidate",
            name="skills",
        ),
        migrations.RemoveField(
            model_name="candidate",
            name="title",
        ),
        migrations.RemoveField(
            model_name="candidate",
            name="top",
        ),
        migrations.AddField(
            model_name="candidate",
            name="Country",
            field=django_countries.fields.CountryField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="candidate",
            name="age",
            field=models.CharField(
                choices=[
                    ("1", "18-25 Years"),
                    ("2", "26-35 Years"),
                    ("3", "36-45 Years"),
                    ("4", "46-55 Years"),
                ],
                default="2",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="bio",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="candidate",
            name="current_salary",
            field=models.CharField(
                choices=[("1", "10-20k"), ("2", "20-30k"), ("3", "30-40k")],
                default="1",
                help_text="10-50k",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="full_name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="candidate",
            name="job_title",
            field=models.CharField(
                help_text="Javascript Developer", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("Full Time", "Full Time"),
                    ("Internship", "Internship"),
                    ("Remote", "Remote"),
                ],
                default="Full Time",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="language",
            field=models.CharField(
                help_text="Eg: English, Hindi", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="phone",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="candidate",
            name="user",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="profile",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="candidate",
            name="email",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="experience_level",
            field=models.CharField(
                choices=[
                    ("Beginner", "Beginner"),
                    ("Intermediate", "Intermediate"),
                    ("Senior", "Senior"),
                ],
                default="Beginner",
                help_text="Eg: Beginner, Senior",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="location",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
