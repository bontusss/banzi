# Generated by Django 4.1 on 2022-08-26 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recruiters", "0020_remove_job_banner_remove_job_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="banner",
            field=models.ImageField(default="df", upload_to="job_banners"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="job",
            name="category",
            field=models.ManyToManyField(to="recruiters.category"),
        ),
        migrations.AddField(
            model_name="job",
            name="company",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jobs",
                to="recruiters.company",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="job",
            name="deadline",
            field=models.DateField(null=True),
        ),
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
        migrations.AddField(
            model_name="job",
            name="skills",
            field=models.ManyToManyField(to="recruiters.skill"),
        ),
        migrations.AddField(
            model_name="job",
            name="type",
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
    ]
