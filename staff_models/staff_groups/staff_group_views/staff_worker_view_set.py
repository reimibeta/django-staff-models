from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from pcr_models.staffs.staff_groups.staff_group_models.staff_worker import StaffWorker
from pcr_models.staffs.staff_groups.staff_group_serializers.staff_worker_serializers import StaffWorkerSerializer


class StaffWorkerViewSet(viewsets.ModelViewSet):
    queryset = StaffWorker.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffWorkerSerializer
