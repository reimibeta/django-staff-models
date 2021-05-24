from rest_flex_fields import FlexFieldsModelSerializer

from pcr_models.staffs.staff_groups.staff_group_models.staff_deliver import StaffDeliver
from pcr_models.staffs.staffs.staff_serializers.staff_serializers import StaffSerializer


class StaffDeliverSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = StaffDeliver
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
