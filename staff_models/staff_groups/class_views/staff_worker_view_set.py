from django.shortcuts import render
from rest_framework import viewsets
from django_rest_framework.pagination import StandardResultsSetPagination

from staff_models.staff_groups.class_models.staff_worker import StaffWorker
from staff_models.staff_groups.class_serializers.staff_worker_serializers import StaffWorkerSerializer


class StaffWorkerViewSet(viewsets.ModelViewSet):
    queryset = StaffWorker.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffWorkerSerializer
