
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    
def review_list(request):
    if request.user.is_authenticated:
        # Display approved reviews and pending reviews by the logged-in user
        reviews = Review.objects.filter(approved=True) | Review.objects.filter(author=request.user)
    else:
        reviews = Review.objects.filter(approved=True)

    return render(request, 'reviews/review_list.html', {'reviews': reviews})



class ReviewCreateView(CreateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'add_review.html'
    success_url = reverse_lazy('review')

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form})

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['review_title', 'content', 'rating']
    template_name = 'add_review.html'
    context_object_name = 'review'
    success_url = reverse_lazy('review')

    def form_valid(self, form):
        # Reset the approval status when the review is edited
        review = form.save(commit=False)
        review.approved = False
        review.save()
        messages.add_message(self.request, messages.SUCCESS, 'Review updated and sent for approval!')
        return super().form_valid(form)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid():
            updated_review = review_form.save(commit=False)
            # Reset approval status when the review is edited
            updated_review.approved = False
            updated_review.save()
            messages.success(request, "Review updated! It will be re-evaluated for approval.")
            return HttpResponseRedirect(reverse('review'))
        else:
            messages.error(request, "Error updating your review!")

    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': review_form, 'review': review})




class ReviewDeleteView(SuccessMessageMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review')  # Redirect to the review list page
    success_message = "Review deleted successfully!"

@login_required
def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
