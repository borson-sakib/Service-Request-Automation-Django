# Generated by Django 4.0.4 on 2024-07-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Mobile',
            field=models.CharField(max_length=200, null=True),
        ),
    ]