from django.shortcuts import render

from Apps.Users.models import User, Student


def home(request):
    data = {}
    # user = User.objects.get(id=request.user.id)
    # user.is_data_completed = False
    # user.save()
    return render(request, 'pages/index.html', data)
