from django.views.generic import ListView
from calendarapp.models import Shift

class AllShiftsListView(ListView):
    """ All shift list views """

    template_name = "calendarapp/shifts_list.html"
    model = Shift

    def get_queryset(self):
        return Shift.objects.get_all_shifts(user=self.request.user)


class RunningShiftsListView(ListView):
    """ Running shifts list view """

    template_name = "calendarapp/shifts_list.html"
    model = Shift

    def get_queryset(self):
        return Shift.objects.get_running_shifts(user=self.request.user)