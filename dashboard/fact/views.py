import requests as re
from django.shortcuts import render, redirect

from apps.courses.models.facts import FactsModel
from dashboard.fact.forms import FactForm


def fact_list(requests, pk=None):
    forms = FactForm()
    if pk:
        html = 'detail'
        lists = FactsModel.objects.get(pk=pk)
        forms = FactForm(instance=lists)
    else:
        html = 'fact'
        lists = FactsModel.objects.all()
    ctx = {
        "lists": lists,
        "forms": forms
    }
    return render(requests, f"dashboard/fact/{html}.html", ctx)


def add(requests):
    forms = FactForm()
    if requests.POST:
        form = FactForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dash_facts_list')
        else:
            print(form.errors)
    ctx = {
        "forms": forms
    }
    return render(requests, "dashboard/fact/form.html", ctx)


