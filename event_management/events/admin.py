from django.contrib import admin
from .models import Event, EventParticipant, EventRating

# Register your models here.
admin.site.register(Event)
admin.site.register(EventParticipant)
admin.site.register(EventRating)