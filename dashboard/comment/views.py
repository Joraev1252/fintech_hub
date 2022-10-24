import requests as re
from django.shortcuts import render, redirect

from apps.teachers.models.comments import CommentsModel
from dashboard.comment.forms import CommentForm


def comment(requests):
    root = CommentsModel.objects.all()
    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/commend/commend.html', ctx)


def commend_add(requests):
    forms = CommentForm()
    if requests.POST:
        form = CommentForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('dash_comment')
    ctx = {
        "forms": forms
    }
    return render(requests, f"dashboard/commend/form.html", ctx)
