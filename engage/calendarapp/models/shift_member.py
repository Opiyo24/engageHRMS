from django.db import models

from accounts.models import User
from calendarapp.models import Shift, ShiftAbstract


class ShiftMember(ShiftAbstract):
    """ Shift member model """

    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name="shifts")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="shift_members"
    )

    class Meta:
        unique_together = ["shift", "user"]

    def __str__(self):
        return str(self.user)
