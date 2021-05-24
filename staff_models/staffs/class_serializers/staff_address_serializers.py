from rest_flex_fields import FlexFieldsModelSerializer


# product size serializer
from staff_models.staffs.class_models.staff_address import StaffAddress


class StaffAddressSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = StaffAddress
        fields = ['id', 'url', 'staff', 'address', 'map', 'city', 'country']
