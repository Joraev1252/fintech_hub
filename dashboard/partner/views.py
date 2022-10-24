from django.shortcuts import render, redirect

from apps.contact.models.contact import ContactModel
from apps.partners.models.partners import PartnersModel
from dashboard.partner.forms import PartnerForm


def partner_list(requests):
    contact = PartnersModel.objects.all()
    ctx = {
        "contact": contact
    }
    return render(requests, f"dashboard/partners/contact.html", ctx)


def partner_add(requests):
    forms = PartnerForm()
    if requests.POST:
        form = PartnerForm(requests.POST)
        if form.is_valid():
            form.save()
        return redirect('dash_partner_list')
    ctx = {
        "forms": forms
    }
    return render(requests, f"dashboard/partners/form.html", ctx)


def part_edit(requests, pk):
    root = PartnersModel.objects.get(pk=pk)
    forms = PartnerForm(instance=root)
    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/partners/detail.html', ctx)

