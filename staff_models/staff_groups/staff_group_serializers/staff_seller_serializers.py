from rest_flex_fields import FlexFieldsModelSerializer

from pcr_models.staffs.staff_groups.staff_group_models.staff_seller import StaffSeller
from pcr_models.staffs.staffs.staff_serializers.staff_serializers import StaffSerializer


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
