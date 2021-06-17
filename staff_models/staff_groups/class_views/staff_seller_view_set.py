from django.shortcuts import render
from rest_framework import viewsets
from django_rest_framework.pagination import StandardResultsSetPagination

from staff_models.staff_groups.class_models.staff_seller import StaffSeller
from staff_models.staff_groups.class_serializers.staff_seller_serializers import StaffSellerSerializer


class StaffSellerViewSet(viewsets.ModelViewSet):
    queryset = StaffSeller.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffSellerSerializer
