# Generated by Django 4.2.13 on 2024-05-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_company_account_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company_account",
            name="password1",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="company_account",
            name="password2",
            field=models.CharField(default="", max_length=100),
        ),
    ]
