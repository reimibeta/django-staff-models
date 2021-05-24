from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView

from staff_models.staffs.class_serializers.staff_auth_serializers import StaffTokenObtainPairSerializer


class StaffTokenVerifyViewSet(TokenVerifyView):
    pass


class StaffTokenObtainPairViewSet(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = StaffTokenObtainPairSerializer

    def post(self, request, **kwargs):
        # serializer = self.serializer_class(data=request.POST)
        serializer = self.serializer_class(data=request.data)
        # print(request.data['name'])
        if serializer.is_valid():  # raise_exception=ValueError
            pass
            # print(serializer.data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.data)
            serializer_dict = {
                "token": {},
                "user": {},
                'msg_error': serializer.errors,
                # "msg_error": {},
                "success": False,
            }
            # if 'name' in request.data and request.data['name'] == "" and 'password' in request.data and request.data['password'] == "":
            #     serializer_dict['msg_error'] = {
            #         "name": "This field may not be blank..",
            #         "password": "This field may not be blank.."
            #     }
            # elif 'name' in request.data and request.data['name'] == "":
            #     serializer_dict['msg_error'] = {"name": "This field may not be blank.."}
            # elif 'password' in request.data and request.data['password'] == "":
            #     serializer_dict['msg_error'] = {"password": "This field may not be blank.."}
            return Response(serializer_dict, status=status.HTTP_400_BAD_REQUEST)
