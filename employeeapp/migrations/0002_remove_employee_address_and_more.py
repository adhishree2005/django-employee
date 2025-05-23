# Generated by Django 5.2 on 2025-04-10 11:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='bank_account_no',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='projects_done_in_year',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='term_in_company',
        ),
        migrations.AddField(
            model_name='employee',
            name='account_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='base_pay',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='employee',
            name='completed_projects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='family_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='given_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='home_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='joined_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(default='Employee', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Unspecified', 'Unspecified')], default='Unspecified', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='work_email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='years_employed',
            field=models.IntegerField(default=0, help_text='How long the person has worked here (in years)'),
        ),
    ]
