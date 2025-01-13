from django.contrib import admin
from .models import SemesterNote

@admin.register(SemesterNote)
class SemesterNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'regulation', 'branch', 'semester', 'pdf')
    list_filter = ('regulation', 'branch', 'semester')
    search_fields = ('title', 'regulation', 'branch', 'semester')
