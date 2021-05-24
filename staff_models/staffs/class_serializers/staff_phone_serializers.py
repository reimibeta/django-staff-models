from rest_flex_fields import FlexFieldsModelSerializer

# product size serializer
from staff_models.staffs.class_models.staff_phone import StaffPhone


class StaffPhoneSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = StaffPhone
        fields = ['id', 'url', 'staff', 'phone']
