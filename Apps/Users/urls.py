from django.urls import path

from Apps.Users.views import profile

app_name = 'users'


urlpatterns = [
    path('<str:username>', profile, name='profile'),
]
