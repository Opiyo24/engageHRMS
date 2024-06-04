from django.forms import ModelForm, DateInput, TimeInput
from calendarapp.models import Event, EventMember, Shift, ShiftMember
from django import forms

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "start_time", "end_time"]
        # datetime-local is a HTML5 input type
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event description",
                }
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]


class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = ["title", "start_time", "end_time"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter shift title"}
            ),
            "start_time": TimeInput(
                attrs={"type": "time", "class": "form-control"},
                format="%H:%M",
            ),
            "end_time": TimeInput(
                attrs={"type": "time", "class": "form-control"},
                format="%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ShiftForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 time input to time field
        self.fields["start_time"].input_formats = ("%H:%M",)
        self.fields["end_time"].input_formats = ("%H:%M",)


class AddShiftMemberForm(forms.ModelForm):
    class Meta:
        model = ShiftMember
        fields = ["user"]