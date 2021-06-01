from datetime_utils.date_time import DateTime
from django.db import models

from staff_models.staffs.staffs.class_models.staff import Staff


class StaffWorker(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    assigned_date = models.DateField(default=DateTime.datenow)
    # removed_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.staff)