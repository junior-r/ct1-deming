from allauth.account.forms import SignupForm
from django import forms
from django_countries.fields import CountryField

from Apps.Users.models import User, Institution, Teacher, Student

GENDER_OPTIONS = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)


class CreateUserForm(SignupForm):
    USER_TYPE_CHOICES = (
        ('student', 'Estudiante'),
        ('teacher', 'Profesor'),
        ('company', 'Compañía/Institución'),
    )
    image = forms.ImageField(label='Imagen de perfil', required=False, widget=forms.FileInput(attrs={

    }))
    email = forms.EmailField(label='Correo electrónico', required=True, widget=forms.EmailInput(attrs={

    }))
    username = forms.CharField(label='Nombre de usuario', required=True, widget=forms.TextInput(attrs={

    }))
    first_name = forms.CharField(label='Nombres', required=True, widget=forms.TextInput(attrs={

    }))
    last_name = forms.CharField(label='Apellidos', required=True, widget=forms.TextInput(attrs={

    }))
    phone = forms.CharField(label='Número de teléfono (Código de país)', required=True, widget=forms.TextInput(attrs={

    }))
    password1 = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(attrs={

    }))
    password2 = forms.CharField(label='Contraseña (de nuevo)', required=True, widget=forms.PasswordInput(attrs={

    }))
    user_type = forms.ChoiceField(label='Tipo de usuario', choices=USER_TYPE_CHOICES, required=True,
                                  widget=forms.Select(attrs={

                                  }))

    def save(self, request):
        user = super().save(request)
        user.image = self.cleaned_data['image']
        user.user_type = self.cleaned_data['user_type']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user

    class Meta:
        model = User
        fields = ['image', 'email', 'username', 'first_name', 'last_name', 'phone', 'password1', 'password2']


class InstitutionCreationForm(forms.ModelForm):
    manager_name = forms.CharField(label='Nombres del Director', required=True, widget=forms.TextInput(attrs={

    }))
    manager_phone = forms.CharField(label='Teléfono del Director', required=True, widget=forms.TextInput(attrs={

    }))
    manager_email = forms.CharField(label='E-mail del Director', required=True, widget=forms.TextInput(attrs={

    }))
    city = forms.CharField(label='Ciudad', required=True, widget=forms.TextInput(attrs={

    }))
    country = CountryField()

    class Meta:
        model = Institution
        fields = ['manager_name', 'manager_phone', 'manager_email', 'city', 'country']


class TeacherCreationForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Género', required=True, choices=GENDER_OPTIONS, widget=forms.Select(attrs={

    }))
    birth_date = forms.DateField(label='Fecha de Nacimiento', required=True, widget=forms.DateInput(attrs={
        'type': 'date',
    }))
    country = CountryField()

    class Meta:
        model = Teacher
        fields = ['gender', 'birth_date', 'country']


class StudentCreationForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Género', required=True, choices=GENDER_OPTIONS, widget=forms.Select(attrs={

    }))
    birth_date = forms.DateField(label='Fecha de Nacimiento', required=True, widget=forms.DateInput(attrs={
        'type': 'date',
    }))
    level = forms.CharField(label='Nivel de Estudios', required=True, widget=forms.TextInput(attrs={

    }))
    country = CountryField()

    class Meta:
        model = Student
        fields = ['gender', 'birth_date', 'level', 'country']


class DateInput(forms.DateInput):
    input_type = 'date'
