from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventParticipant, EventRating
from .forms import EventRatingForm, EventForm, EventParticipantForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date_and_time = request.POST.get('date_and_time')
        location = request.POST.get('location')
        description = request.POST.get('description')
        is_public = request.POST.get('is_public')
        creator = request.user

        event = Event(name=name, date_and_time=date_and_time, location=location,
                      description=description, is_public=is_public, creator=creator)
        event.save()

        return redirect('event_list')

    return render(request, 'events/create_event.html')

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.date_and_time = request.POST.get('date_and_time')
        event.location = request.POST.get('location')
        event.description = request.POST.get('description')
        event.is_public = request.POST.get('is_public')
        event.save()

        return redirect('event_list')

    return render(request, 'events/edit_event.html', {'event': event})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    
    return render(request, 'events/delete_event.html', {'event': event})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    ratings = EventRating.objects.filter(event=event)
    
    if request.method == 'POST':
        form = EventRatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            author = request.user
            
            event_rating = EventRating(rating=rating, comment=comment, event=event, author=author)
            event_rating.save()
    
    else:
        form = EventRatingForm()
    
    return render(request, 'events/event_detail.html', {'event': event, 'ratings': ratings, 'form': form})

def participant_list(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants = event.eventparticipant_set.all()

    return render(request, 'participant_list.html', {'event': event, 'participants': participants})

@login_required
def create_participant(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = EventParticipantForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']

            if not EventParticipant.objects.filter(event=event, user=user).exists():
                event_participant = EventParticipant(event=event, user=user)
                event_participant.save()
                messages.success(request, f'{user.username} pridėtas kaip dalyvis!')
            else:
                messages.warning(request, f'{user.username} jau yra dalyvis šventėje.')
            return redirect('participant_list', event_id=event_id)
    else:
        form = EventParticipantForm()

    return render(request, 'create_participant.html', {'event': event, 'form': form})

@login_required
def event_ratings(request, event_id):
    event = Event.objects.get(pk=event_id)
    ratings = EventRating.objects.filter(event=event)

    if request.method == 'POST':
        form = EventRatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']

            event_rating = EventRating(event=event, author=request.user, rating=rating, comment=comment)
            event_rating.save()
            messages.success(request, 'Jūsų įvertinimas pridėtas sėkmingai!')
            return redirect('event_ratings', event_id=event_id)
    else:
        form = EventRatingForm()

    return render(request, 'event_ratings.html', {'event': event, 'ratings': ratings, 'form': form})


