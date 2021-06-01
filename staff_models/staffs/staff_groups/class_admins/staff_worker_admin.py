from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter

from staff_models.staffs.staff_groups.class_models.staff_worker import StaffWorker
from staff_models.staffs.staffs.class_models.staff_phone import StaffPhone


class StaffWorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'staff',
        'staff_phones',
        'assigned_date',
        'is_active'
    )
    list_display_links = ['staff', ]
    list_per_page = 25

    def staff_phones(self, obj):
        # return ", ".join(obj.staff.staffphones)
        # return obj.staff.staffphones[0]
        phones = []
        staffphones = StaffPhone.objects.filter(staff=obj.id)
        for phone in staffphones:
            phones.append(phone.phone)
        return ", ".join(phones)

    list_filter = (
        # for ordinary fields
        ('assigned_date', DropdownFilter),
        ('is_active', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('staff', RelatedDropdownFilter),
    )


admin.site.register(StaffWorker, StaffWorkerAdmin)
