# Generated by Django 4.0.4 on 2023-02-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeInfo', '0012_status_code_forwarded_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_request',
            name='application_status',
            field=models.IntegerField(default='0', max_length=100, null=True),
        ),
    ]