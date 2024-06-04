from .event_list import AllEventsListView, RunningEventsListView
from .other_views import (
    CalendarViewNew,
    CalendarView,
    create_event,
    EventEdit,
    event_details,
    add_eventmember,
    EventMemberDeleteView,
    delete_event,
    next_week,
    next_day,
)
from .shift_list import AllShiftsListView, RunningShiftsListView
from .other_shift_views import (
    create_shift, 
    ShiftEdit, 
    shift_details, 
    add_shiftmember, 
    ShiftMemberDeleteView, 
    delete_shift, 
    next_week_shift, 
    next_day_shift
)


__all__ = [
    AllEventsListView,
    RunningEventsListView,
    CalendarViewNew,
    CalendarView,
    create_event,
    EventEdit,
    event_details,
    add_eventmember,
    EventMemberDeleteView,
    delete_event,
    next_week,
    next_day,
    AllShiftsListView,
    RunningShiftsListView,
    create_shift,
    ShiftEdit,
    shift_details,
    add_shiftmember,
    ShiftMemberDeleteView,
    delete_shift,
    next_week_shift,
    next_day_shift
]
