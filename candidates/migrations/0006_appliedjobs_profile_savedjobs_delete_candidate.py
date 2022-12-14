# Generated by Django 4.1 on 2022-08-25 08:11

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("recruiters", "0005_alter_job_category_alter_job_skills"),
        ("candidates", "0005_remove_candidate_id_remove_candidate_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppliedJobs",
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
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applied_job",
                        to="recruiters.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applied_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("full_name", models.CharField(max_length=100, null=True)),
                (
                    "job_title",
                    models.CharField(
                        help_text="Javascript Developer", max_length=100, null=True
                    ),
                ),
                ("bio", models.TextField(null=True)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="user", unique=True
                    ),
                ),
                ("phone", models.CharField(max_length=15, null=True)),
                ("email", models.CharField(max_length=100, null=True)),
                (
                    "Country",
                    django_countries.fields.CountryField(max_length=100, null=True),
                ),
                (
                    "resume",
                    models.FileField(blank=True, null=True, upload_to="resumes"),
                ),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("Full Time", "Full Time"),
                            ("Internship", "Internship"),
                            ("Remote", "Remote"),
                        ],
                        default="Full Time",
                        max_length=50,
                    ),
                ),
                (
                    "experience_level",
                    models.CharField(
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
                (
                    "current_salary",
                    models.CharField(
                        choices=[("1", "10-20k"), ("2", "20-30k"), ("3", "30-40k")],
                        default="1",
                        help_text="10-50k",
                        max_length=50,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        help_text="Eg: English, Hindi", max_length=100, null=True
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "age",
                    models.CharField(
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
                (
                    "looking_for",
                    models.CharField(
                        choices=[
                            ("Full Time", "Full Time"),
                            ("Internship", "Internship"),
                            ("Remote", "Remote"),
                        ],
                        default="Remote",
                        max_length=50,
                    ),
                ),
                (
                    "qualifications",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="candidates.qualification",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SavedJobs",
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
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="saved_job",
                        to="recruiters.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="saved",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Candidate",
        ),
    ]
