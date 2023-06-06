import os

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


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

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return os.path.join(settings.MEDIA_URL, 'user_profile_placeholder.jpg')

    def __str__(self):
        return f'{self.get_username()}'
