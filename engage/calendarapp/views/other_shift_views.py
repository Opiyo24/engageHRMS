from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from calendarapp.models import Shift
from calendarapp.forms import ShiftForm, AddShiftMemberForm
from .other_views import get_date, prev_month, next_month
from calendarapp.utils import Calendar
from calendarapp.models import ShiftMember, Shift


class ShiftCalendarView(LoginRequiredMixin, generic.ListView):
    login_url = "accounts:company-login"
    model = Shift
    template_name = "calendarapp/shift_calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


@login_required(login_url="signup")
def create_shift(request):
    form = ShiftForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        Shift.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendarapp:shift_calendar"))
    return render(request, "shift.html", {"form": form})


class ShiftEdit(generic.UpdateView):
    model = Shift
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "shift.html"


@login_required(login_url="signup")
def shift_details(request, shift_id):
    shift = Shift.objects.get(id=shift_id)
    shiftmember = ShiftMember.objects.filter(shift=shift)
    context = {"shift": shift, "shiftmember": shiftmember}
    return render(request, "shift-details.html", context)


def add_shiftmember(request, shift_id):
    forms = AddShiftMemberForm()
    if request.method == "POST":
        forms = AddShiftMemberForm(request.POST)
        if forms.is_valid():
            member = ShiftMember.objects.filter(shift=shift_id)
            shift = Shift.objects.get(id=shift_id)
            if member.count() <= 9:
                user = forms.cleaned_data["user"]
                ShiftMember.objects.create(shift=shift, user=user)
                return redirect("calendarapp:shift_calendar")
            else:
                print("--------------User limit exceed!-----------------")
    context = {"form": forms}
    return render(request, "add_shiftmember.html", context)


class ShiftMemberDeleteView(generic.DeleteView):
    model = ShiftMember
    template_name = "shift_delete.html"
    success_url = reverse_lazy("calendarapp:shift_calendar")


class ShiftCalendarViewNew(LoginRequiredMixin, generic.View):
    login_url = "accounts:company-login"
    template_name = "calendarapp/shift_calendar.html"
    form_class = ShiftForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        shifts = Shift.objects.get_all_shifts(user=request.user)
        shifts_month = Shift.objects.get_running_shifts(user=request.user)
        shift_list = []
        for shift in shifts:
            shift_list.append(
                {
                    "id": shift.id,
                    "title": shift.title,
                    "start": shift.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": shift.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": shift.description,
                }
            )
        context = {"form": forms, "shifts": shift_list, "shifts_month": shifts_month}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms =self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("calendarapp:shift_calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


def delete_shift(request, shift_id):
    shift = get_object_or_404(Shift, id=shift_id)
    if request.method == 'POST':
        shift.delete()
        return JsonResponse({'message': 'Shift sucess delete.'})
    else:
        return JsonResponse({'message': 'Error!'}, status=400)

def next_week_shift(request, shift_id):
    shift = get_object_or_404(Shift, id=shift_id)
    if request.method == 'POST':
        next = shift
        next.id = None
        next.start_time += timedelta(days=7)
        next.end_time += timedelta(days=7)
        next.save()
        return JsonResponse({'message': 'Sucess!'})
    else:
        return JsonResponse({'message': 'Error!'}, status=400)

def next_day_shift(request, shift_id):
    shift = get_object_or_404(Shift, id=shift_id)
    if request.method == 'POST':
        next = shift
        next.id = None
        next.start_time += timedelta(days=1)
        next.end_time += timedelta(days=1)
        next.save()
        return JsonResponse({'message': 'Sucess!'})
    else:
        return JsonResponse({'message': 'Error!'}, status=400)