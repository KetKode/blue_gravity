# Generated by Django 5.1 on 2024-08-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Content",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=300)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("G", "game"),
                            ("V", "video"),
                            ("A", "artwork"),
                            ("M", "music"),
                        ],
                        max_length=1,
                    ),
                ),
                ("thumbnail_url", models.URLField(blank=True, null=True)),
                ("content_url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
