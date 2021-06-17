from rest_flex_fields import FlexFieldsModelSerializer

# product size serializer
from staff_models.staffs.class_models.staff import Staff
from staff_models.staffs.class_models.staff_address import StaffAddress
from django_rest_framework.key_related_field import key_related_field


class StaffAddressSerializer(FlexFieldsModelSerializer):
    # staff = key_related_field.related_field(
    #     Staff.objects.filter(is_active=True)
    # )

    class Meta:
        model = StaffAddress
        fields = ['id', 'url', 'staff', 'address', 'map', 'city', 'country']
