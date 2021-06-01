from rest_flex_fields import FlexFieldsModelSerializer

from staff_models.staffs.staff_groups.class_models.staff_seller import StaffSeller
from staff_models.staffs.staffs.class_serializers.staff_serializers import StaffSerializer


class StaffSellerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = StaffSeller
        fields = [
            'id',
            'staff',
            'assigned_date',
            'removed_date',
            'is_active'
        ]
        expandable_fields = {
            'staff': StaffSerializer
        }
