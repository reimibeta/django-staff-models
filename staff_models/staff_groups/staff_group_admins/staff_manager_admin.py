from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from pcr_models.staffs.staff_groups.staff_group_models.staff_manager import StaffManager


class StaffManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'assigned_date', 'removed_date', 'is_active')
    list_display_links = ['staff', ]
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('assigned_date', DropdownFilter),
        ('is_active', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('staff', RelatedDropdownFilter),
    )


admin.site.register(StaffManager, StaffManagerAdmin)
