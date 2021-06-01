from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from staff_models.staffs.staffs.class_models.staff import Staff
from staff_models.staffs.staffs.class_serializers.staff_serializers import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffSerializer
