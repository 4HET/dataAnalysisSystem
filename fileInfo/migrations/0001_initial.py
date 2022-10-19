# Generated by Django 4.1 on 2022-10-11 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="file_info",
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
                ("file_name", models.CharField(max_length=20)),
                ("file_id", models.CharField(max_length=20)),
                ("file_user", models.CharField(max_length=20)),
            ],
        ),
    ]