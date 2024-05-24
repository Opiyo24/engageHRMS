# Generated by Django 4.2.13 on 2024-05-24 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0007_alter_employee_address_alter_employee_end_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="company_account",
            name="user",
            field=models.OneToOneField(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
