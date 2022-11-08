# Generated by Django 4.1.1 on 2022-09-21 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Context",
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
                ("name", models.CharField(max_length=100, verbose_name="이름")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 일자"),
                ),
            ],
        ),
    ]