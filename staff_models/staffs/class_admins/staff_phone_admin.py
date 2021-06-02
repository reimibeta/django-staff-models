from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from staff_models.staffs.class_models.staff_phone import StaffPhone


class StaffPhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'phone')
    list_display_links = ['staff', ]
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('phone', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('staff', RelatedDropdownFilter),
    )


admin.site.register(StaffPhone, StaffPhoneAdmin)


class StaffPhoneAdminInline(admin.TabularInline):
    model = StaffPhone
    extra = 0
