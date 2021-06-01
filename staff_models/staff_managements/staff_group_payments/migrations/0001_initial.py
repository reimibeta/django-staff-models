# Generated by Django 3.1.7 on 2021-05-27 13:42

import datetime_utils.date_time
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import applications.staff_managements.staff_group_payments.class_projects.staff_payment_status_choice


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallets', '0001_initial'),
        ('staff_groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffWorkerPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(default=datetime_utils.date_time.DateTime.datenow)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('pay_status', models.CharField(choices=[('DAILY', 'daily'), ('MONTHLY', 'monthly'), ('YEARLY', 'yearly'), ('OPTIONAL', 'optional')], default=applications.staff_managements.staff_group_payments.class_projects.staff_payment_status_choice.StaffPaymentStatusChoice['DAILY'], max_length=60)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallets.wallet')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff_groups.staffworker')),
            ],
        ),
    ]
