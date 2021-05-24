from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from staff_models.staffs.staff_models.staff_address import StaffAddress


class StaffAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'address', 'map', 'city', 'country')
    list_display_links = ['staff', ]
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('address', DropdownFilter),
        ('city', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('staff', RelatedDropdownFilter),
    )


admin.site.register(StaffAddress, StaffAddressAdmin)


class StaffAddressAdminInline(admin.TabularInline):
    model = StaffAddress
    extra = 0
