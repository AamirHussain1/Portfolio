from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')

    else:
        form = ContactForm()

    context = {'form': form,
               'contact': 'active'}
    return render(request, 'core/contact.html', context)
