from django.urls import path
from .views import (
    ReviewUpdateView,
    ReviewDeleteView,
    add_review,
    edit_review,
    review_list
)

urlpatterns = [
    path('', review_list, name='review'),
    path('add/', add_review, name='add_review'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('reviews/<int:review_id>/edit/', edit_review, name='edit_review'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
