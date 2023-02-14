# Generated by Django 4.0.4 on 2023-02-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeInfo', '0010_alter_service_request_approved_by_ciso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='operations_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_request_employee_id', models.CharField(max_length=100)),
                ('service_request_id', models.CharField(max_length=100)),
                ('service_request_time', models.DateTimeField(max_length=100)),
                ('approved_hod', models.CharField(default='0', max_length=100)),
                ('approved_hod_at', models.DateTimeField(max_length=100, null=True)),
                ('approved_ciso', models.CharField(default='0', max_length=100)),
                ('approved_ciso_at', models.DateTimeField(max_length=100, null=True)),
                ('approved_cto', models.CharField(default='0', max_length=100)),
                ('approved_cto_at', models.DateTimeField(max_length=100, null=True)),
                ('executed', models.CharField(default='0', max_length=100)),
                ('executed_at', models.DateTimeField(max_length=100, null=True)),
                ('current_status', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='status_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.CharField(max_length=10)),
                ('status_meaning', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='service_request',
            name='service_request_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
