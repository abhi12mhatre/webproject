# Generated by Django 4.2.6 on 2023-10-22 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('room_number', models.CharField(max_length=10)),
                ('rent', models.FloatField(default=0.0)),
                ('deposit', models.FloatField(default=0.0)),
                ('details', models.TextField()),
                ('address', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_manager.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tenant',
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
                ('agreement_start_date', models.DateField()),
                ('agreement_end_date', models.DateField()),
                ('estate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estate_manager.estate')),
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
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('amount', models.FloatField(default=0.0)),
                ('balance', models.FloatField(default=0.0)),
                ('is_paid', models.BooleanField(default=False)),
                ('estate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estate_manager.estate')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estate_manager.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
