from rest_flex_fields import FlexFieldsModelSerializer

from staff_models.staff_groups.class_models.staff_worker import StaffWorker
from staff_models.staffs.class_serializers.staff_serializers import StaffSerializer


class StaffWorkerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = StaffWorker
        fields = [
            'id',
            'url',
            'staff',
            'assigned_date',
            # 'removed_date',
            'is_active'
        ]
        expandable_fields = {
            'staff': StaffSerializer
        }
