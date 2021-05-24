from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from pcr_models.staffs.staffs.staff_models.staff_phone import StaffPhone
from pcr_models.staffs.staffs.staff_serializers.staff_phone_serializers import StaffPhoneSerializer


class StaffPhoneViewSet(viewsets.ModelViewSet):
    queryset = StaffPhone.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffPhoneSerializer
