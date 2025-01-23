from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils.decorators import method_decorator

from .models import Review
from .forms import ReviewForm


# ListView to display reviews
class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        """
        Show approved reviews or the user's reviews.
        """
        if self.request.user.is_authenticated:
            return Review.objects.filter(approved=True) | Review.objects.filter(author=self.request.user)
        return Review.objects.filter(approved=True)


@login_required
def add_review(request):
    """
    Function-based view to add a new review.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, "Review added! It will be reviewed for approval.")
            return redirect('review')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form})


# Restricting access to the update view to the author
@method_decorator(login_required, name='dispatch')
class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'add_review.html'
    success_url = reverse_lazy('review')

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        # Ensure the logged-in user is the author
        if review.author != request.user:
            return HttpResponseForbidden("You are not allowed to edit this review.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        # Reset the approval status when edited
        review.approved = False
        review.save()
        messages.success(self.request, "Review updated and sent for approval!")
        return super().form_valid(form)


@login_required
def edit_review(request, review_id):
    """
    Function-based view to edit a review.
    """
    review = get_object_or_404(Review, pk=review_id)

    # Restrict access to the review's author
    if review.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid():
            updated_review = review_form.save(commit=False)
            # Reset approval status when edited
            updated_review.approved = False
            updated_review.save()
            messages.success(request, "Review updated! It will be re-evaluated for approval.")
            return HttpResponseRedirect(reverse('review'))
        else:
            messages.error(request, "Error updating your review!")

    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': review_form, 'review': review})


# Restricting access to the delete view to the author
@method_decorator(login_required, name='dispatch')
class ReviewDeleteView(SuccessMessageMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review')  # Redirect to the review list page
    success_message = "Review deleted successfully!"

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        # Ensure the logged-in user is the author
        if review.author != request.user:
            return HttpResponseForbidden("You are not allowed to delete this review.")
        return super().dispatch(request, *args, **kwargs)


# Filtering reviews by the logged-in user
@login_required
def review_list(request):
    """
    Custom review list function to filter reviews for logged-in users.
    """
    if request.user.is_authenticated:
        # Display approved reviews and pending reviews by the logged-in user
        reviews = Review.objects.filter(approved=True) | Review.objects.filter(author=request.user)
    else:
        reviews = Review.objects.filter(approved=True)

    return render(request, 'reviews/review_list.html', {'reviews': reviews})