from django.shortcuts import render, redirect

from apps.courses.models.courses import CourseModel
from dashboard.courses.forms import CourseForm
from dashboard.courses.service import get_courses


def courses_lists(requests, pk=None):
    if pk:
        course = CourseModel.objects.get(pk=pk)
        html = 'detail'
    else:
        html = 'courses'
        course = CourseModel.objects.all()
    context = {
        "courses": course
    }

    return render(requests, f'dashboard/courses/{html}.html', context)


def add_edit(requests, pk=None):
    forms = CourseForm()
    if pk:
        lists = CourseModel.objects.get(pk=pk)
        forms = CourseForm(instance=lists)
    else:
        lists = None
    if requests.POST:
        if pk:
            form = CourseForm(requests.POST, instance=lists)
        else:
            form = CourseForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_courses')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/courses/form.html', ctx)


def c_detail(requests, pk):
    # lists =
    pass