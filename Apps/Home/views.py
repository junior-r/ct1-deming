from django.shortcuts import render

from Apps.Users.models import User


def home(request):
    data = {}
    return render(request, 'pages/index.html', data)
