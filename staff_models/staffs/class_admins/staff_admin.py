from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from staff_models.staffs.class_admins.staff_address_admin import StaffAddressAdminInline
from staff_models.staffs.class_admins.staff_phone_admin import StaffPhoneAdminInline
from staff_models.staffs.class_models.staff import Staff
from staff_models.staffs.class_models.staff_phone import StaffPhone


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phones', 'is_active',)
    list_display_links = ['name', ]
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        # ('name', DropdownFilter),
        ('is_active', DropdownFilter),
        # ('name', DropdownFilter),
        ('staff_phone__phone', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('user', RelatedDropdownFilter),
        ('staff_address', RelatedDropdownFilter),
    )

    search_fields = ['name', ]

    def phones(self, obj):
        arr = []
        phones = StaffPhone.objects.filter(staff=obj.id).all()
        if phones:
            for phone in phones:
                arr.append(phone.phone)
            return ", ".join(arr)
        else:
            return "not provide"

    inlines = [
        StaffPhoneAdminInline,
        StaffAddressAdminInline
    ]


admin.site.register(Staff, StaffAdmin)
