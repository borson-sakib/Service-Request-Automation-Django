# Generated by Django 3.2.13 on 2024-03-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_request',
            name='submitted_by',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
