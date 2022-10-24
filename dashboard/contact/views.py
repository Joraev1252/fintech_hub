import requests as re
from django.shortcuts import render, redirect

from apps.contact.models.contact import ContactModel
from dashboard.contact.forms import ContactForm1


def contact_handler(requests):
    root = ContactModel.objects.all()

    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/contact/contact.html', ctx)


def contact_add(requests):
    forms = ContactForm1()
    if requests.POST:
        form = ContactForm1(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_contact')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/contact/form.html', ctx)



