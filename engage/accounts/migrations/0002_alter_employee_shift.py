# Generated by Django 4.2.13 on 2024-06-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="shift",
            field=models.CharField(default="None", max_length=100),
        ),
    ]
