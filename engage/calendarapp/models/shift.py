from datetime import datetime
from django.db import models
from django.urls import reverse

from calendarapp.models import ShiftAbstract
from accounts.models import User


class ShiftManager(models.Manager):
    """ Shift manager """

    def get_all_shifts(self, user):
        shifts = Shift.objects.filter(user=user, is_active=True, is_deleted=False)
        return shifts

    def get_running_shifts(self, user):
        running_shifts = Shift.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_shifts


class Shift(ShiftAbstract):
    """ Shift model """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shifts")
    title = models.CharField(max_length=200)
    # description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = ShiftManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:shift-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:shift-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
