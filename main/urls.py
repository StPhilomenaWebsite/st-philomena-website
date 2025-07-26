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
    path('music_album_launch/', views.music_album_launch, name='music_album_launch'),
    path('academic_calendar/', views.academic_calendar, name='academic_calendar'),



    path('blog/', views.blog, name='blog'),

]
