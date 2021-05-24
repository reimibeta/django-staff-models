from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from staff_models.staff_groups.class_models.staff_manager import StaffManager
from staff_models.staff_groups.class_serializers.staff_manager_serializers import StaffManagerSerializer


class StaffManagerViewSet(viewsets.ModelViewSet):
    queryset = StaffManager.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffManagerSerializer
