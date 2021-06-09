from rest_flex_fields import FlexFieldsModelSerializer

from staff_models.staff_groups.class_models.staff_manager import StaffManager
from staff_models.staffs.class_serializers.staff_serializers import StaffSerializer


class StaffManagerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = StaffManager
        fields = [
            'id',
            'staff',
            'assigned_date',
            # 'removed_date',
            'is_active'
        ]
        expandable_fields = {
            'staff': StaffSerializer
        }
