from django.shortcuts import render
from .models import DiaryPage, DiaryIntro

def diary_view(request):
    # Fetch the intro settings (or create a default if empty)
    intro, created = DiaryIntro.objects.get_or_create(id=1)
    # Fetch all pages in order (1, 2, 3...)
    pages = DiaryPage.objects.all().order_by('page_number')
    
    return render(request, 'diary/index.html', {
        'intro': intro,
        'pages': pages
    })