# Generated by Django 4.1.3 on 2022-11-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodel', '0003_alter_user_branch_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch_code',
            field=models.CharField(max_length=200),
        ),
    ]
