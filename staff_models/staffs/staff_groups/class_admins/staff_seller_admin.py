from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from staff_models.staffs.staff_groups.class_models.staff_seller import StaffSeller


class StaffSellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'assigned_date', 'is_active')
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


admin.site.register(StaffSeller, StaffSellerAdmin)
