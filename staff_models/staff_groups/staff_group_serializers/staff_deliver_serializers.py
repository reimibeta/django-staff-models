from rest_flex_fields import FlexFieldsModelSerializer

from staff_models.staff_groups.staff_group_models.staff_deliver import StaffDeliver
from staff_models.staffs.staff_serializers.staff_serializers import StaffSerializer


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
