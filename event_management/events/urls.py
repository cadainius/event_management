from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('event', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('event/<int:event_id>/delete_event', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/participants/', views.participant_list, name='participant_list'),
    path('event/<int:event_id>/participants/create_participant/', views.create_participant, name='create_participant'),
  #  path('event/<int:event_id>/participants/create_participant/', views.showusername, name='create'),
    path('event/<int:event_id>/ratings/', views.event_ratings, name='event_ratings'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)