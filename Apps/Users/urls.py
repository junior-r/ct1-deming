from django.urls import path

from Apps.Users.views import profile, complete_data, check_user_data, list_institutions

app_name = 'users'


urlpatterns = [
    path('check_user_data/', check_user_data, name='check_user_data'),
    path('list_institutions/', list_institutions, name='list_institutions'),
    path('<str:username>/', profile, name='profile'),
    path('complete_data/<int:user_id>/', complete_data, name='complete_data'),
]
