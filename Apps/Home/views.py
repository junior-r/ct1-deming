from django.shortcuts import render

from Apps.Users.models import User, Student


def home(request):
    data = {}
    return render(request, 'pages/index.html', data)
