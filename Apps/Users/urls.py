from django.urls import path

from Apps.Users.views import profile, complete_data, check_user_data

app_name = 'users'


urlpatterns = [
    path('check_user_data/', check_user_data, name='check_user_data'),
    path('<str:username>/', profile, name='profile'),
    path('complete_data/<int:user_id>/', complete_data, name='complete_data'),
]
