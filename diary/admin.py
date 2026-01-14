from django.contrib import admin
from .models import DiaryPage, DiaryIntro

admin.site.register(DiaryIntro)

@admin.register(DiaryPage)
class DiaryPageAdmin(admin.ModelAdmin):
    list_display = ('page_number', 'question')