from rest_flex_fields import FlexFieldsModelSerializer

# product size serializer
from rest_framework_utils.key_related_field import key_related_field

from staff_models.staffs.class_models.staff import Staff
from staff_models.staffs.class_models.staff_phone import StaffPhone


class StaffPhoneSerializer(FlexFieldsModelSerializer):
    # staff = key_related_field.related_field(
    #     Staff.objects.filter(is_active=True)
    # )

    class Meta:
        model = StaffPhone
        fields = ['id', 'url', 'staff', 'phone']
