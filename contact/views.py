from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm  # Import your form class


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form (e.g., save to database, send email)
            form.save()  # Example if your form is a ModelForm
            messages.success
            (request, 'Your message has been sent successfully!'
                'I endeavor to respond within 2 working days.')
            # Redirect to the same page or another page
            return redirect('contact')
        else:
            messages.error
            (request, 'There was an error submitting your form.'
                'Please check and try again.')
    else:
        form = ContactForm()  # Instantiate an empty form

    # Pass the form instance and messages to the template
    return render(request, 'contact.html', {'contact_form': form})
