from django.shortcuts import render
from .forms import RegistrationForm, ContactForm, BookForm 

def display_forms(request):

    registration_form = RegistrationForm()
    contact_form = ContactForm()
    book_form = BookForm()

 
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        contact_form = ContactForm(request.POST)
        book_form = BookForm(request.POST)
    
    return render(request, 'book_form_app/forms_display.html', {
        'registration_form': registration_form,
        'contact_form': contact_form,
        'book_form': book_form,
    })