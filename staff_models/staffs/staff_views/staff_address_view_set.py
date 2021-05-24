from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from pcr_models.staffs.staffs.staff_models.staff_address import StaffAddress
from pcr_models.staffs.staffs.staff_serializers.staff_address_serializers import StaffAddressSerializer


class StaffAddressViewSet(viewsets.ModelViewSet):
    queryset = StaffAddress.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffAddressSerializer
