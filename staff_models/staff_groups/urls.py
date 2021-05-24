from django.conf.urls import url
from django.urls import path, include

from rest_framework import routers

from pcr_models.staffs.staff_groups import views

router = routers.DefaultRouter()
router.register('staff-manager', views.StaffManagerViewSet)
router.register('staff-deliver', views.StaffDeliverViewSet)
router.register('staff-seller', views.StaffSellerViewSet)
router.register('staff-worker', views.StaffWorkerViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
