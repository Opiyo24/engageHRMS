# Generated by Django 4.2.13 on 2024-05-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0006_contract_type_department_title_delete_contract_types_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="address",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="end_date",
            field=models.DateField(null=True),
        ),
    ]
