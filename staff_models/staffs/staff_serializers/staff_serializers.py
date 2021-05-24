from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from pcr_models.staffs.staffs.staff_models.staff import Staff
from pcr_models.staffs.staffs.staff_serializers.staff_address_serializers import StaffAddressSerializer
from pcr_models.staffs.staffs.staff_serializers.staff_phone_serializers import StaffPhoneSerializer


class StaffSerializer(FlexFieldsModelSerializer):
    staff_phone = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    staff_address = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Staff
        fields = [
            'id',
            'url',
            'name',
            'is_active',
            'staff_phone',
            'staff_address'
        ]
        expandable_fields = {
            'staff_phone': (StaffPhoneSerializer, {'many': True}),
            'staff_address': StaffAddressSerializer
        }
