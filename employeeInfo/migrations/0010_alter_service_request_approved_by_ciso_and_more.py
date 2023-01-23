# Generated by Django 4.0.4 on 2023-01-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeInfo', '0009_alter_service_request_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_request',
            name='approved_by_CISO',
            field=models.CharField(default='No', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_request',
            name='approved_by_CTO',
            field=models.CharField(default='No', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_request',
            name='approved_by_HOB',
            field=models.CharField(default='No', max_length=100, null=True),
        ),
    ]
