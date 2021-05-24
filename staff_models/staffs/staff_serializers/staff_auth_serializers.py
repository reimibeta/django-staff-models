from collections import OrderedDict

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': {
            "token": {},
            "user": {},
            "message": "username and password not found.",
            "success": False,
        },
    }

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(StaffTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        # data.update({'user': self.user.username})
        # data.update({'id': self.user.id})
        # and everything else you want to send in the response
        # user_queryset = User.objects.filter(email=attrs['email']).first()
        user_queryset = User.objects.first()

        user = {
            "id": user_queryset.id,
            "name": user_queryset.name,
            "email": user_queryset.email,
            "first_name": user_queryset.first_name,
            "last_name": user_queryset.last_name,
            # "photo": HOST_URL + user_photo_queryset.photo.url
        }

        # user = Response(user_queryset)
        # from django.forms.order_models import model_to_dict
        # model_to_dict(user_queryset),

        return {
            "token": data,
            "user": user,
            "message": "Login success.",
            "success": True
        }
        # serializers.serialize("user", user)
