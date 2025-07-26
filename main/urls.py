from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('admissions/', views.admissions, name='admissions'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('announcements/', views.announcements, name='announcements'),
    path('about_developer/', views.about_developer, name='about_developer'),
    path('music-album-launch/', views.music_album_launch, name='music_album_launch'),
    path('music-album-launch/', views.academic_calendar, name='music_album_launch'),



    path('blog/', views.blog, name='blog'),

]
