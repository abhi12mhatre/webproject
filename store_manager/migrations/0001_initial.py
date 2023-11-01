# Generated by Django 4.2.6 on 2023-10-22 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_manager.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_manager.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'In Active')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
                ('rate', models.FloatField(default=0.0)),
                ('amount', models.FloatField(default=0.0)),
                ('discount', models.FloatField(default=0.0)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Outward'), (1, 'Inward')], default=0)),
                ('order_status', models.PositiveSmallIntegerField(choices=[(0, 'New'), (1, 'Accepted'), (2, 'In Process'), (3, 'Ready'), (4, 'Dispatched'), (5, 'Delivered'), (6, 'Cancelled')], default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_manager.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_manager.store')),
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
                ('is_paid', models.BooleanField(default=False)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_manager.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
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
                ('delivery_address', models.TextField(blank=True, null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Customer'), (1, 'Vendor')], default=0)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_manager.store')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]