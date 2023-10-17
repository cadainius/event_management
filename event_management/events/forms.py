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
        if rating < 1 or rating > 5:
            raise ValidationError("Reitingas turi būti nuo 1 iki 5.")
        return rating

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date_and_time', 'location', 'description', 'is_public']

    is_public = forms.BooleanField(required=False, initial=True)

    def clean_is_public(self):
        is_public = self.cleaned_data['is_public']
        if is_public is None:
            return False
        return is_public

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



