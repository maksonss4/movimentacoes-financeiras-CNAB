# Generated by Django 4.1.5 on 2023-01-30 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transactions",
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
                ("type", models.CharField(max_length=10)),
                ("date", models.DateField()),
                ("value", models.CharField(max_length=10)),
                ("cpf", models.IntegerField()),
                ("card", models.CharField(max_length=12)),
                ("hour", models.TimeField()),
                ("store_owner", models.CharField(max_length=14)),
                ("store_name", models.CharField(max_length=19)),
            ],
        ),
    ]
