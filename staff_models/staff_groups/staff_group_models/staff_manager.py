from datetime_utils.date_time import DateTime
from django.db import models

from pcr_models.staffs.staffs.staff_models.staff import Staff


class StaffManager(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    assigned_date = models.DateField(default=DateTime.datenow)
    removed_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.staff)
