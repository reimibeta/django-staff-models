from django.db import models

from staff_models.staffs.staff_models.staff import Staff


class StaffPhone(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_phone')
    # region = models.CharField(max_length=10, blank=True, null=True, editable=False)
    # country_code = models.CharField(max_length=100, blank=True, null=True, editable=False)
    # national = models.CharField(max_length=100, blank=True, null=True, editable=False)
    # national_number = models.CharField(max_length=100, blank=True, null=True, editable=False)
    # international = models.CharField(max_length=100, blank=True, null=True, editable=False)
    # international_standard = models.CharField(max_length=100, blank=True, null=True, editable=False)
    # type = models.CharField(max_length=100, blank=True, null=True, editable=False)
    phone = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = (('staff', 'phone'),)

    def __str__(self):
        return '{}({})'.format(self.staff, self.phone)