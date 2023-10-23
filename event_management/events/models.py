from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

class EventParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class EventRating(models.Model):
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)