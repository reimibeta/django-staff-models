from decimal import Decimal

from datetime_utils.date_time import DateTime
from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

# from pcr_models.products.product_accounts.models import ProductAccount
from wallet_models.wallet_models.wallet import Wallet

from pcr_models.classes.balances.outlets.balance_outlet import BalanceOutlet
from pcr_models.staffs.staff_group_payments.staff_group_payment_classes.staff_payment_status_choice import \
    StaffPaymentStatusChoice
from pcr_models.staffs.staff_groups.staff_group_models.staff_worker import StaffWorker


class StaffWorkerPayment(models.Model):
    account = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffWorker, on_delete=models.CASCADE)
    pay_date = models.DateField(default=DateTime.datenow)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    pay_status = models.CharField(
        max_length=60,
        choices=StaffPaymentStatusChoice.choices(),
        default=StaffPaymentStatusChoice.DAILY,
    )

    def __str__(self):
        return "{}".format(self.staff)


@receiver(post_save, sender=StaffWorkerPayment)
def add(sender, instance, created, **kwargs):
    if created:
        # account
        BalanceOutlet.outlet(
            amount=instance.amount,
            account_pk=instance.account.id
        )


@receiver(pre_save, sender=StaffWorkerPayment)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        old_value = StaffWorkerPayment.objects.get(id=instance.id)
        # account
        if instance.account.id == old_value.account.id:
            BalanceOutlet.update(
                new_amount=instance.amount,
                old_amount=old_value.amount,
                account_pk=instance.account.id
            )
        else:
            # refund
            BalanceOutlet.refund(old_value.amount, old_value.account.id)
            # outlet
            BalanceOutlet.outlet(instance.amount, instance.account.id)


@receiver(pre_delete, sender=StaffWorkerPayment)
def delete(sender, instance, using, **kwargs):
    old_value = StaffWorkerPayment.objects.get(id=instance.id)
    BalanceOutlet.refund(old_value.amount, old_value.account.id)
