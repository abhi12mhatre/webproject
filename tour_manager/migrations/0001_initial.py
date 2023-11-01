# Generated by Django 4.2.6 on 2023-10-22 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
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
                ('aadhar_card', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=20)),
                ('details', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('adult', models.PositiveSmallIntegerField(default=0)),
                ('child', models.PositiveSmallIntegerField(default=0)),
                ('date', models.DateField()),
                ('cost', models.FloatField(default=0.0)),
                ('amount', models.FloatField(default=0.0)),
                ('discount', models.FloatField(default=0.0)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour_manager.customer')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour_manager.package')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('amount', models.FloatField(default=0.0)),
                ('balance', models.FloatField(default=0.0)),
                ('payment_mode', models.PositiveSmallIntegerField(choices=[(0, 'Cash'), (1, 'UPI'), (2, 'Card'), (3, 'Cheque'), (4, 'Draft'), (5, 'NEFT'), (6, 'IMPS')], default=0)),
                ('payment_type', models.PositiveSmallIntegerField(choices=[(0, 'Advance'), (0, 'Installment')], default=0)),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour_manager.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
