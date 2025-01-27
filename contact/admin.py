from django.contrib import admin
from contact.models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):  # Ensure it's admin.ModelAdmin
    list_display = ('name', 'email', 'subject', 'read')  
    search_fields = ('name', 'email', 'subject')  
    list_filter = ('read',)