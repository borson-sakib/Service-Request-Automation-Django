# Generated by Django 4.0.4 on 2023-01-15 10:46

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_no', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('branch_code', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=100)),
                ('branch_division_name', models.CharField(max_length=100)),
                ('pa_no', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('self_type', models.CharField(blank=True, choices=[('self', 'Self'), ('selfwithservice', 'Self with Service'), ('serviceprovider', 'Service Provider'), ('team', 'Team'), ('visitor', 'Visitor')], max_length=100)),
                ('from_date', models.DateField(blank=True, max_length=100)),
                ('to_date', models.DateField(blank=True, max_length=100)),
                ('to_date_check', models.BooleanField(blank=True, max_length=100)),
                ('from_time', models.TimeField(blank=True, max_length=100)),
                ('to_time', models.TimeField(blank=True, max_length=100)),
                ('to_time_check', models.BooleanField(blank=True, max_length=100)),
                ('reason', models.CharField(blank=True, max_length=100)),
                ('details', models.CharField(blank=True, max_length=100)),
                ('vendor_name', models.CharField(blank=True, max_length=100)),
                ('name1', models.CharField(blank=True, max_length=100)),
                ('contact_number1', models.CharField(blank=True, max_length=100)),
                ('name2', models.CharField(blank=True, max_length=100)),
                ('contact_number2', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('EmployeeName', models.CharField(max_length=200)),
                ('EmployeeDesignation', models.CharField(max_length=200)),
                ('EmpFunctionalDesignation', models.CharField(max_length=200)),
                ('Placeofposting', models.CharField(max_length=200)),
                ('EmployeeID', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('signature', models.ImageField(blank=True, upload_to='images/signatures')),
                ('pi', models.ImageField(blank=True, upload_to='images/pi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
