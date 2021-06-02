from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from staff_models.staffs.class_models.staff_address import StaffAddress
from staff_models.staffs.class_serializers.staff_address_serializers import StaffAddressSerializer


class StaffAddressViewSet(viewsets.ModelViewSet):
    queryset = StaffAddress.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffAddressSerializer
