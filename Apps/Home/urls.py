from django.urls import path
from Apps.Home.views import home


app_name = 'home'

urlpatterns = [
    path('', home, name='home')
]
