from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import EventRating, Event, EventParticipant
from django.core.exceptions import ValidationError

class EventRatingForm(forms.ModelForm):
    class Meta:
        model = EventRating
        fields = ['rating', 'comment']

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 10:
            raise ValidationError("The rating must be between 1 and 10.")
        return rating

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date_and_time', 'location', 'description', 'is_public', 'image']

class EventParticipantForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Pasirinkite dalyvį')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')



