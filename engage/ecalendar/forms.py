from django.forms import ModelForm, DateInput
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


# class TimeForm(ModelForm):
#   class Meta:
#     model = Time
#     widgets = {
#       'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),#edit for hours and minutes only
#       'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#     }
#     fields = '__all__'

#   def __init__(self, *args, **kwargs):
#     super(TimeForm, self).__init__(*args, **kwargs)
#     self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#     self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)



# class ShiftForm(ModelForm):
#   class Meta:
#     model = Shift
#     widgets = {
#       'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#       'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#     }
#     fields = '__all__'

#   def __init__(self, *args, **kwargs):
#     super(ShiftForm, self).__init__(*args, **kwargs)
#     self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#     self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)