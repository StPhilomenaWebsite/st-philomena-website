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
    path('form1-selection/', views.form1_selection, name='form1_selection'),
    path('events/term3/', views.term3_events, name='events_2024-2025_term_3'),
    path('events/term1/', views.term1_events, name='events_2025-2026_term_1'),
    path('nsonkhano_makolo_2025/', views.nsonkhano_makolo_2025, name='nsonkhano_makolo_2025'),
    path('mankhwala_katemera_2025/', views.mankhwala_katemera_2025, name='mankhwala_katemera_2025'),
    path('drug_vaccine_2025/', views.drug_vaccine_2025, name='drug_vaccine_2025'),




    path('blog/', views.blog, name='blog'),

]
