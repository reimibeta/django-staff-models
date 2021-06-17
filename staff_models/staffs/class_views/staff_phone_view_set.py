from rest_framework import viewsets
from django_rest_framework.pagination import StandardResultsSetPagination

from staff_models.staffs.class_models.staff_phone import StaffPhone
from staff_models.staffs.class_serializers.staff_phone_serializers import StaffPhoneSerializer


class StaffPhoneViewSet(viewsets.ModelViewSet):
    queryset = StaffPhone.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffPhoneSerializer
