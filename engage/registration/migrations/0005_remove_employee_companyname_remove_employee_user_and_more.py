# Generated by Django 4.2.13 on 2024-05-21 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0004_rename_id_company_companyid_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="companyname",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="user",
        ),
        migrations.DeleteModel(
            name="Company",
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]