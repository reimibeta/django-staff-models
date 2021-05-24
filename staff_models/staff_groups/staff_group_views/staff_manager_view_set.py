from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from pcr_models.staffs.staff_groups.staff_group_models.staff_manager import StaffManager
from pcr_models.staffs.staff_groups.staff_group_serializers.staff_manager_serializers import StaffManagerSerializer


class StaffManagerViewSet(viewsets.ModelViewSet):
    queryset = StaffManager.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffManagerSerializer
