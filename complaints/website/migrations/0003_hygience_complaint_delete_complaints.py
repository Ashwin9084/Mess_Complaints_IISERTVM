# Generated by Django 4.2 on 2023-04-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_cdh_icafe"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hygience_Complaint",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("cdh", models.CharField(max_length=50)),
                ("complaint", models.CharField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name="Complaints",
        ),
    ]