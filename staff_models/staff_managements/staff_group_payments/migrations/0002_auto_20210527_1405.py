# Generated by Django 3.1.7 on 2021-05-27 14:05

import datetime_utils.date_time
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_group_payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffWorkerPaymentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
            ],
        ),
        migrations.AddField(
            model_name='staffworkerpayment',
            name='payment_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff_group_payments.staffworkerpaymentgroup'),
        ),
    ]