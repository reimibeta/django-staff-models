# Generated by Django 3.1.7 on 2021-05-27 13:42

import datetime_utils.date_time
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffs.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffs.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffs.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffDeliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffs.staff')),
            ],
        ),
    ]