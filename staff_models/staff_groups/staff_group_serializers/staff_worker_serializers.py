from rest_flex_fields import FlexFieldsModelSerializer

from staff_models.staff_groups.staff_group_models.staff_worker import StaffWorker
from staff_models.staffs.staff_serializers.staff_serializers import StaffSerializer


class StaffWorkerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = StaffWorker
        fields = [
            'id',
            'url',
            'staff',
            'assigned_date',
            'removed_date',
            'is_active'
        ]
        expandable_fields = {
            'staff': StaffSerializer
        }
