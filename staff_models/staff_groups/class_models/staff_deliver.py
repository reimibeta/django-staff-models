from django_datetime.date_time import datetime
from django.db import models

from staff_models.staffs.class_models.staff import Staff


class StaffDeliver(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    assigned_date = models.DateField(default=datetime.dnow())
    # removed_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.staff)
