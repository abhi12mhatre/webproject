# Generated by Django 4.2.6 on 2023-10-22 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], default=0)),
                ('dob', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('alternate_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('department', models.PositiveSmallIntegerField(choices=[(0, 'Sales'), (1, 'Admin'), (2, 'Support'), (3, 'IT'), (4, 'Engineer'), (5, 'HR'), (6, 'Management')], default=1)),
                ('position', models.PositiveSmallIntegerField(choices=[(0, 'Intern'), (1, 'Executive'), (2, 'Sr Executive'), (3, 'Team Lead'), (4, 'Manager'), (5, 'CTO'), (6, 'CFO'), (7, 'CEO')], default=0)),
                ('joining_date', models.DateField()),
                ('leaving_date', models.DateField(blank=True, null=True)),
                ('available_leaves', models.FloatField(default=0.0)),
                ('emp_salary', models.FloatField(default=0.0)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.company')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='e_manager', to='hrms.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('base_amount', models.FloatField(default=0.0)),
                ('deduction', models.FloatField(default=0.0)),
                ('pay_amount', models.FloatField(default=0.0)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeaveTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.FloatField(default=0.0)),
                ('unpaid_leave_count', models.FloatField(default=0.0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]