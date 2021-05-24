from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)
