from enum import Enum


class StaffPaymentStatusChoice(Enum):
    DAILY = "daily"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    OPTIONAL = "optional"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)