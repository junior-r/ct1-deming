from django.shortcuts import render


def home(request):
    data={}
    return render(request, 'pages/index.html', data)
