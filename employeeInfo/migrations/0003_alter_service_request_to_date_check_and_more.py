# Generated by Django 4.0.4 on 2023-01-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeInfo', '0002_alter_service_request_to_date_check_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_request',
            name='to_date_check',
            field=models.BooleanField(default=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_request',
            name='to_time_check',
            field=models.BooleanField(blank=True, default=False, max_length=100, null=True),
        ),
    ]
