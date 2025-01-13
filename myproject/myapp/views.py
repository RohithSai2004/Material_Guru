from django.shortcuts import render, get_object_or_404
from .models import SemesterNote
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)  # Define the logger at the module level

def index(request):
    return render(request, 'index.html')

def sem_view(request):
    return render(request, 'sem.html')

def get_semester_notes(request):
    regulation = request.GET.get('regulation')
    branch = request.GET.get('branch')
    semester = request.GET.get('semester')

    logger.info(f"Received parameters - Regulation: {regulation}, Branch: {branch}, Semester: {semester}") 

    if not (regulation and branch and semester):
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    notes = SemesterNote.objects.filter(
        regulation=regulation,
        branch=branch,
        semester=semester
    ) 

    if not notes:
        return JsonResponse({'notes': []}, status=200)  # Return empty list if no notes found
    note_data = []
    for note in notes:
        note_data.append({
            'title': note.title,
            'pdf_url': note.pdf.url,  # Provide the URL for the PDF file
        })

    return JsonResponse({'notes': note_data}, status=200)

def download_pdf(request, pdf_path):
    try:
        file_path = os.path.join(settings.MEDIA_ROOT, pdf_path)
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_path)}"'
            return response
    except FileNotFoundError:
        return HttpResponseNotFound('PDF file not found.')