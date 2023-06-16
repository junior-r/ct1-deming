import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from Apps.Users.forms import InstitutionCreationForm, TeacherCreationForm, StudentCreationForm
from Apps.Users.models import User, Student, Teacher, Institution


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = user.get_instance()

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
        data = serialize('json', [user, ])
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
            if user.user_type == 'company':
                form = InstitutionCreationForm(request.POST, request.FILES, instance=user_instance)
            elif user.user_type == 'teacher':
                form = TeacherCreationForm(request.POST, request.FILES, instance=user_instance)
            else:
                form = StudentCreationForm(request.POST, request.FILES, instance=user_instance)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user.is_data_completed = True
                instance.user.save()
                instance.save()
                message = f'Datos completados correctamente'
                new_user_data = {'id': instance.user.id, 'username': instance.user.get_username(),
                                 'completed_data': user.is_data_completed}
                response = JsonResponse(
                    {'message': message, 'user': new_user_data, 'object': 'UserData', 'icon': 'success'})
                response.status_code = 201
                return response
            else:
                message = f'No se pudo registrar los datos'
                user_data = {'id': 0, 'username': None}
                response = JsonResponse(
                    {'message': message, 'user': user_data, 'error': form.errors, 'icon': 'error'})
                response.status_code = 400
                return response
        else:
            return redirect('home:home')

    return render(request, 'Users/complete_data.html', data)


@login_required
def list_institutions(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        institutions = Institution.objects.all()
        institutions_list = []
        for institution in institutions:
            data_institution = {}
            data_institution['institution_user_id'] = institution.user.id
            data_institution['institution_user_username'] = institution.user.get_username()
            data_institution['institution_id'] = institution.id
            data_institution['institution_name'] = institution.user.get_full_name()
            data_institution['institution_manager_name'] = institution.manager_name
            data_institution['current_user_id'] = request.user.id
            data_institution['current_user_username'] = request.user.username
            institutions_list.append(data_institution)

        data = json.dumps(institutions_list)
        return HttpResponse(data, 'application/json')
    return redirect('users:profile', request.user.username)


@login_required
def request_to_join(request, institution_id, user_id):
    print(institution_id, user_id)
    user = get_object_or_404(User, id=user_id)
    user_instance = user.get_instance()
    if user.user_type in ['student', 'teacher']:
        institution = get_object_or_404(Institution, id=institution_id)
        data = {
            'user': user,
            'institution': institution,
            'user_instance': user_instance,
        }

        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax and request.method == 'POST':
            description = request.POST.get('description')
            user_instance.description = description
            user_instance.institution = institution
            user_instance.save()

            message = f'Tu solicitud de unión fué enviada a {institution.user.get_full_name().capitalize()}'
            user_data = {'id': user_instance.id, 'full_name': user_instance.user.get_full_name(),
                         'is_joined': user_instance.joined}
            response = JsonResponse(
                {'message': message, 'user': user_data, 'object': 'RequestJoin', 'icon': 'success'})
            response.status_code = 201
            return response

        return render(request, 'Users/request_to_join.html', data)
    else:
        messages.error(request, 'No puedes unirte a una institución o compañia si ya eres una de estas.')
        return redirect('users:profile', user.username)
