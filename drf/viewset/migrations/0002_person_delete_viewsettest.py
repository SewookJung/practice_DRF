# Generated by Django 4.1.1 on 2022-10-21 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drf_viewset", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=128, verbose_name="이름")),
                ("age", models.PositiveSmallIntegerField(verbose_name="나이")),
                ("addr", models.CharField(max_length=128, verbose_name="주소")),
                ("addr_detail", models.CharField(max_length=128, verbose_name="상세 주소")),
            ],
            options={
                "db_table": "person",
            },
        ),
        migrations.DeleteModel(
            name="ViewsetTest",
        ),
    ]