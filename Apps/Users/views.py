from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from Apps.Users.forms import InstitutionCreationForm, TeacherCreationForm, StudentCreationForm
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
def check_user_data(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        user = get_object_or_404(User, id=request.user.id)
        data = serialize('json', [user,])
        return HttpResponse(data, 'application/json')
    return redirect('home:home')


@login_required
def complete_data(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.user_type == 'company':
        user_instance = Institution.objects.get(user_id=user.id)
        form = InstitutionCreationForm(instance=user_instance)
    elif user.user_type == 'teacher':
        user_instance = Teacher.objects.get(user_id=user.id)
        form = TeacherCreationForm(instance=user_instance)
    else:
        user_instance = Student.objects.get(user_id=user.id)
        form = StudentCreationForm(instance=user_instance)

    data = {
        'user': user,
        'form': form,
    }

    if request.method == 'POST':
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            print('is ajax')
            if user.user_type == 'company':
                form = InstitutionCreationForm(request.POST, request.FILES, instance=user_instance)
            elif user.user_type == 'teacher':
                form = TeacherCreationForm(request.POST, request.FILES, instance=user_instance)
            else:
                form = StudentCreationForm(request.POST, request.FILES, instance=user_instance)
            if form.is_valid():
                print('is valid')
                instance = form.save(commit=False)
                # instance.user = user
                instance.user.is_data_completed = True
                instance.user.save()
                instance.save()
                message = f'Datos completados correctamente'
                new_user_data = {'id': instance.user.id, 'username': instance.user.get_username(), 'completed_data': user.is_data_completed}
                response = JsonResponse(
                    {'message': message, 'user': new_user_data, 'object': 'UserData', 'icon': 'success'})
                response.status_code = 201
                return response
            else:
                print('is not valid')
                message = f'No se pudo registrar los datos'
                user_data = {'id': 0, 'username': None}
                response = JsonResponse(
                    {'message': message, 'user': user_data, 'error': form.errors, 'icon': 'error'})
                response.status_code = 400
                return response
        else:
            print('is not ajax')
            return redirect('home:home')

    return render(request, 'Users/complete_data.html', data)

