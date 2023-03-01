# Generated by Django 4.1.6 on 2023-02-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tv_shows", "0003_ratingtv"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ratingtv",
            name="rate",
            field=models.CharField(
                choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
                max_length=100,
                null=True,
            ),
        ),
    ]