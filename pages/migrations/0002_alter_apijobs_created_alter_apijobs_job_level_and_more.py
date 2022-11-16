# Generated by Django 4.1 on 2022-08-21 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apijobs",
            name="created",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="apijobs",
            name="job_level",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="apijobs",
            name="job_type",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="apijobs",
            name="location",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="apijobs",
            name="slug",
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name="apijobs",
            name="url",
            field=models.URLField(null=True),
        ),
    ]