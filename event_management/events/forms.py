from django import forms
from django.contrib.auth.models import User
from .models import EventRating, Event, EventParticipant

class EventRatingForm(forms.ModelForm):
    class Meta:
        model = EventRating
        fields = ['rating', 'comment']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date_and_time', 'location', 'description', 'is_public']

class EventParticipantForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Pasirinkite dalyvį')

