from allauth.account.forms import SignupForm
from django import forms

from Apps.Users.models import User


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
    user_type = forms.ChoiceField(label='Tipo de usuario', choices=USER_TYPE_CHOICES, required=True, widget=forms.Select(attrs={

    }))

    def save(self, request):
        user = super().save(request)
        user.image = self.cleaned_data['image']
        user.user_type = self.cleaned_data['user_type']
        print(self.cleaned_data)
        print(self.cleaned_data['image'], self.cleaned_data['user_type'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['image', 'email', 'username', 'first_name', 'last_name', 'phone', 'password1', 'password2']

