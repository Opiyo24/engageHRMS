from django.urls import path
from . import views

app_name = "calendarapp"

urlpatterns = [
    path("calender/", views.CalendarViewNew.as_view(), name="calendar"),
    path("calenders/", views.CalendarView.as_view(), name="calendars"),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('next_week/<int:event_id>/', views.next_week, name='next_week'),
    path('next_day/<int:event_id>/', views.next_day, name='next_day'),
    path("event/new/", views.create_event, name="event_new"),
    path("event/edit/<int:pk>/", views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path(
        "add_eventmember/<int:event_id>", views.add_eventmember, name="add_eventmember"
    ),
    path(
        "event/<int:pk>/remove",
        views.EventMemberDeleteView.as_view(),
        name="remove_event",
    ),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all_events"),
    path(
        "running-event-list/",
        views.RunningEventsListView.as_view(),
        name="running_events",
    ),
    path("shift/new/", views.create_shift, name="shift_new"),
    path("shift/edit/<int:pk>/", views.ShiftEdit.as_view(), name="shift_edit"),
    path("shift/<int:shift_id>/details/", views.shift_details, name="shift-detail"),
    path(
        "add_shiftemployee/<int:shift_id>", views.add_shiftmember, name="add_shiftemployee"
    ),
    path(
        "shift/<int:pk>/remove",
        views.ShiftMemberDeleteView.as_view(),
        name="remove_shift",
    ),
    path("all-shift-list/", views.AllShiftsListView.as_view(), name="all_shifts"),
    path(
        "running-shift-list/",
        views.RunningShiftsListView.as_view(),
        name="running_shifts",
    ),
    path('delete_shift/<int:shift_id>/', views.delete_shift, name='delete_shift'),
]