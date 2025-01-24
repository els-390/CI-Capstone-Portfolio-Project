from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'review_title', 'rating', 'created_on', 'approved')
    list_filter = ('author', 'rating', 'created_on')
    search_fields = (
        'author', 'review_title', 'user__username', 'content'
    )
