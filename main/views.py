from django.shortcuts import render

# Create your views here.
# Each function renders a page
def home(request):
    return render(request, 'main/home.html')

def results(request):
    return render(request, 'main/results.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def about_developer(request):
    return render(request, 'main/about_developer.html')


def events(request):
    return render(request, 'main/events.html')


def announcements(request):
    return render(request, 'main/announcements.html')


def blog(request):
    return render(request, 'main/blog.html')

def academic_calendar(request):
    return render(request, 'main/academic_calendar.html')

def music_album_launch(request):
    return render(request, 'main/music_album_launch.html')

def form1_selection(request):
    return render(request, 'main/form1_selection.html')

def term3_events(request):
    return render(request, 'main/events_2024-2025_term_3.html')

def term1_events(request):
    return render(request, 'main/events_2025-2026_term_1.html')

def nsonkhano_makolo_2025(request):
    return render(request, 'main/nsonkhano_makolo_2025.html')

def mankhwala_katemera_2025(request):
    return render(request, 'main/mankhwala_katemera_2025.html')

def drug_vaccine_2025(request):
    return render(request, 'main/drug_vaccine_2025.html')





