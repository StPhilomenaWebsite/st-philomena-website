from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

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

def download_form1_pdf(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password != 'proviess':
            return HttpResponse("Incorrect password! You cannot download the PDF.", status=403)

        # Render HTML with all student data
        html_string = render_to_string('main/form1_selection.html', {})  # create a separate template for PDF if needed

        # Create a PDF
        html = HTML(string=html_string)
        result = html.write_pdf()

        # Create HTTP response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Form1_Selection.pdf"'
        response.write(result)
        return response

    return HttpResponse("Invalid request method.", status=400)


