from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'reviewer_name',
        'review_title',
        'rating',
        'created_on',
        'approved',
    )
    list_filter = (
        'author',
        'rating',
        'created_on',
        'approved',
    )
    search_fields = (
        'author__username',
        'review_title',
        'reviewer_name',
        'content',
    )
