from rest_framework import viewsets
from django_rest_framework.pagination import StandardResultsSetPagination

from staff_models.staff_groups.class_models.staff_deliver import StaffDeliver
from staff_models.staff_groups.class_serializers.staff_deliver_serializers import StaffDeliverSerializer


class StaffDeliverViewSet(viewsets.ModelViewSet):
    queryset = StaffDeliver.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffDeliverSerializer
