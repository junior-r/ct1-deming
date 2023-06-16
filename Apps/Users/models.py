import os

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


def user_directory_image_path(instance, filename):
    image_name = 'Users/Images/{0}/{1}'.format(instance, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, image_name)
    if os.path.exists(full_path):
        os.remove(full_path)

    return image_name


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Estudiante'),
        ('teacher', 'Profesor'),
        ('company', 'Compañía/Institución'),
    )
    image = models.ImageField(upload_to=user_directory_image_path)
    phone = models.CharField(max_length=20)
    user_type = models.CharField(max_length=25, choices=USER_TYPE_CHOICES)
    is_data_completed = models.BooleanField(default=False)

    def get_instance(self):
        if self.user_type == 'company':
            return Institution.objects.get(user_id=self.id)
        elif self.user_type == 'teacher':
            return Teacher.objects.get(user_id=self.id)
        else:
            return Student.objects.get(user_id=self.id)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return os.path.join(settings.MEDIA_URL, 'user_profile_placeholder.jpg')

    def get_user_type(self):
        if self.user_type == 'company':
            return '<span class="bg-yellow-100 text-yellow-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-yellow-900 dark:text-yellow-300">Institución</span>'
        elif self.user_type == 'teacher':
            return '<span class="bg-green-100 text-green-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300">Profesor</span>'
        else:
            return '<span class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">Estudiante</span>'

    def __str__(self):
        return f'{self.get_username()}'


class Institution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=250, null=False, blank=False)
    manager_phone = models.CharField(max_length=20, null=False, blank=False)
    manager_email = models.EmailField(null=False, blank=False, unique=True)
    city = models.CharField(blank=False, null=False)
    country = CountryField(blank=False, null=False)

    def __str__(self):
        return f"Institution: {self.user.get_full_name()}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='students', related_name='students')
    GENDER_OPTIONS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    gender = models.CharField(max_length=20, choices=GENDER_OPTIONS, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    level = models.CharField(max_length=150, blank=True, null=True)
    country = CountryField(blank=True, null=True)

    def __str__(self):
        return f"Student: {self.user.get_full_name()}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='teachers', related_name='teachers')
    GENDER_OPTIONS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    gender = models.CharField(max_length=20, choices=GENDER_OPTIONS, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = CountryField(blank=True, null=True)

    def __str__(self):
        return f"Teacher: {self.user.get_full_name()}"


class RequestToJoin(models.Model):
    STATUS_REQUEST = [
        ('Approved', 'Aprovada'),
        ('Pending', 'Pendiente'),
        ('Rejected', 'Rechazada'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='join_requests',
                             limit_choices_to={'user_type__in': ['student', 'teacher']})
    institution = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requested_joins',
                                    limit_choices_to={'user_type': ['company']})
    status = models.CharField(max_length=25, choices=STATUS_REQUEST, default='Pending')
    date_created = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"Request to join: {self.user} - {self.institution}"


@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    if user.user_type == 'student':
        Student.objects.create(user=user)
    elif user.user_type == 'teacher':
        Teacher.objects.create(user=user)
    elif user.user_type == 'company':
        Institution.objects.create(user=user)


user_signed_up.connect(create_profile)
