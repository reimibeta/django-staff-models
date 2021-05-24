from django.db import models

from staff_models.staffs.staff_models.staff import Staff


class StaffAddress(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='staff_address')
    address = models.CharField(max_length=255)
    map = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.address
