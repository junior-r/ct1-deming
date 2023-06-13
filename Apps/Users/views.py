from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from Apps.Users.models import User, Student, Teacher, Institution


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if user.user_type == 'student':
        user_profile = get_object_or_404(Student, user=user)
    elif user.user_type == 'teacher':
        user_profile = get_object_or_404(Teacher, user=user)
    else:
        user_profile = get_object_or_404(Institution, user=user)

    data = {
        'user': user,
        'user_profile': user_profile,
    }

    return render(request, 'Users/profile.html', data)


@login_required
def complete_data(request, user_id, user_type):
    user = get_object_or_404(User, id=user_id)

