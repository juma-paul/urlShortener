# Generated by Django 5.0.7 on 2024-07-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="long_url",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]