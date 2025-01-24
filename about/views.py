from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


# Create your views here.

def about_me(request):
    """
    Renders the About page.
    """
    about = About.objects.all().order_by('-updated_on').first()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_request = contact_form.save(commit=False)
            contact_request.read = False
            contact_request.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your message has been sent successfully!'
                'I endeavor to respond within 2 working days.'
            )
            contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form,
        },
    )
