from django.contrib import admin
from django.db.models import Sum, Case, When, F, DecimalField
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.urls import path
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter

from staff_models.staff_managements.staff_group_payments.class_models.staff_worker_payment import \
    StaffWorkerPayment, StaffWorkerPaymentGroup


class StaffWorkerPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'staff',
        'pay_amount',
        'pay_date',
        'account',
        'pay_status',
    )
    list_display_links = ['staff', ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        ('pay_status', DropdownFilter),
        ('amount', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('staff', RelatedDropdownFilter),
    )

    def pay_date(self, obj):
        return obj.payment_group.pay_date

    # disable actions
    def has_add_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def pay_amount(self, obj):
        return "{} {}".format(obj.amount, obj.account.currency.currency)

    # Chart
    change_list_template = 'admin/staffs/staff_group_payments/staff_group_payment_list.html'

    # Inject chart data on page load in the ChangeList view
    def changelist_view(self, request, extra_context=None):
        data = self.chart_profit_data()
        # print(data)
        # as_json = json.dumps(list(data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {'data': data}  # "chart_data": as_json,
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_profit_data/", self.admin_site.admin_view(self.chart_profit_data_endpoint)),
        ]
        return extra_urls + urls

    def chart_profit_data_endpoint(self, request):
        data = self.chart_profit_data()
        return JsonResponse(list(data), safe=False)

    def chart_profit_data(self):
        # HourEntries.objects.filter(date__month=this_month).aggregate(Sum("quantity"))
        # payments = StaffWorkerPayment.objects.all()
        # if payments:
        #     data = []
        #     for payment in payments:
        #         if payment.currency.currency == "USD":
        #             data.append(payment.amount)
        #         elif payment.currency.currency == "KHR":
        #             data.append(payment.amount / 4000)
        # for profit in profits:
        #     if profit.order.ordered_date.year == datetime.now().year:
        #         print(profit.order.ordered_date)
        # return (
        #     StaffWorkerPayment.objects
        #         .annotate(date=TruncMonth('pay_date'))
        #         .values('date')
        #         .annotate(amount=Sum('amount'))
        #         .order_by('date')
        # )

        amount = StaffWorkerPayment.objects.annotate(
            date=TruncMonth('payment_group__pay_date')).values('date').annotate(
            # amount=Sum('amount') / float(4000)
            # must use float to retrieve decimal value
            amount=Sum(
                Case(
                    When(account__currency__currency='USD', then=F('amount') / 1),
                    default=F('amount') / float(4000),
                    output_field=DecimalField(),
                )
            )
        ).order_by('date')
        return amount

    # end Profit Chart


admin.site.register(StaffWorkerPayment, StaffWorkerPaymentAdmin)


class StaffWorkerPaymentInlineAdmin(admin.TabularInline):
    extra = 0
    model = StaffWorkerPayment


# group payment
class StaffWorkerPaymentGroupAdmin(admin.ModelAdmin):
    list_display = ['pay_date']
    list_display_links = ['pay_date']
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('pay_date', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('staff', RelatedDropdownFilter),
    )
    inlines = [StaffWorkerPaymentInlineAdmin]
    search_fields = ['pay_date', ]

    # Chart
    change_list_template = 'admin/staffs/staff_group_payments/staff_group_payment_list.html'

    # Inject chart data on page load in the ChangeList view
    def changelist_view(self, request, extra_context=None):
        data = self.chart_profit_data()
        # print(data)
        # as_json = json.dumps(list(data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {'data': data}  # "chart_data": as_json,
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_profit_data/", self.admin_site.admin_view(self.chart_profit_data_endpoint)),
        ]
        return extra_urls + urls

    def chart_profit_data_endpoint(self, request):
        data = self.chart_profit_data()
        return JsonResponse(list(data), safe=False)

    def chart_profit_data(self):
        amount = StaffWorkerPayment.objects.annotate(
            date=TruncMonth('payment_group__pay_date')).values('date').annotate(
            # amount=Sum('amount') / float(4000)
            # must use float to retrieve decimal value
            amount=Sum(
                Case(
                    When(account__currency__currency='USD', then=F('amount') / 1),
                    default=F('amount') / float(4000),
                    output_field=DecimalField(),
                )
            )
        ).order_by('date')
        return amount


admin.site.register(StaffWorkerPaymentGroup, StaffWorkerPaymentGroupAdmin)
