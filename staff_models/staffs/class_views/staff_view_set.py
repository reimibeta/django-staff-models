from rest_framework import viewsets
from django_rest_framework.pagination import StandardResultsSetPagination

from staff_models.staffs.class_models.staff import Staff
from staff_models.staffs.class_serializers.staff_serializers import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffSerializer
