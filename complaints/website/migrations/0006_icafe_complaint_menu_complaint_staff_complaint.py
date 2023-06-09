# Generated by Django 4.2 on 2023-04-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_finance_complaint"),
    ]

    operations = [
        migrations.CreateModel(
            name="Icafe_Complaint",
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
                ("icafe", models.CharField(max_length=50)),
                ("complaint", models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="Menu_Complaint",
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
                ("item", models.CharField(max_length=50)),
                ("complaint", models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="Staff_Complaint",
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
    ]
