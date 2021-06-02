from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers

from staff_models.staffs import views
from staff_models.staffs.class_views.staff_auth_view import StaffTokenVerifyViewSet

router = routers.DefaultRouter()
router.register('staff-phone', views.StaffPhoneViewSet)
router.register('staff-address', views.StaffAddressViewSet)
router.register('staff', views.StaffViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('staff-token/', TokenObtainPairView.as_view()),  # basename='staff-token'),
    path('staff-token/', views.StaffTokenObtainPairViewSet.as_view()),
    path('staff-token-refresh/', TokenRefreshView.as_view()),  # basename='staff-token-refresh'),
    path('staff-token-verify/', StaffTokenVerifyViewSet.as_view()),  # basename='staff-token-verify'),
    # path('staff-token-verify/', TokenVerifyView.as_view()),  # basename='staff-token-verify'),
]
