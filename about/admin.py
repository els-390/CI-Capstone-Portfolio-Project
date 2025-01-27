from django.contrib import admin
from .models import About, ContactRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):  # Ensure it's admin.ModelAdmin
    list_display = ('name', 'email', 'subject', 'read')  
    search_fields = ('name', 'email', 'subject')  
    list_filter = ('read',)
