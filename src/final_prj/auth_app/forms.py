from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class MySigUpForm(UserCreationForm):
    """
    Form for user sign up
    """
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Имя пользователя",
        }),
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
            'placeholder': "Пароль",
        }),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
            'placeholder': "Повторите пароль",
        }),
    )


class SignInForm(forms.Form):
    """
    Form for user sign in
    """
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Имя пользователя",
        })
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Пароль",
        })
    )

    # User login and password validation
    def clean(self):
        super(self.__class__, self).clean()

        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username).first()

        if not user:
            raise forms.ValidationError("Пользователь не найден")

        user = authenticate(**self.cleaned_data)

        if user is None:
            raise forms.ValidationError("Неверный пароль")

        return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    """
    Form for user main data
    """
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "label": "First name",
                "class": "form-control",
                "id": "first_name",
                "placeholder": "First name",
                "required": "required",
            }),
            "last_name": forms.TextInput(attrs={
                "label": "Last name",
                "class": "form-control",
                "id": "last_name",
                "placeholder": "Last name",
                "required": "required",
            }),
            "email": forms.EmailInput(attrs={
                "label": "E-mail",
                "class": "form-control",
                "id": "email",
                "placeholder": "you@example.com",
                "required": "required",
            }),
        }


class ProfileForm(forms.ModelForm):
    """
    Form for user profile data
    """
    class Meta:
        model = Profile
        fields = ["city", "telegram_link", "vk_link", "instagram_link"]
        widgets = {
            "city": forms.TextInput(attrs={
                "label": "City",
                "class": "form-control",
                "id": "city",
                "placeholder": "Minsk",
            }),
            "telegram_link": forms.TextInput(attrs={
                "label": "Telegram",
                "class": "form-control",
                "id": "telegram",
                "placeholder": "@username",
            }),
            "vk_link": forms.TextInput(attrs={
                "label": "VK",
                "class": "form-control",
                "id": "vk",
                "placeholder": "@username",
            }),
            "instagram_link": forms.TextInput(attrs={
                "label": "Instagram",
                "class": "form-control",
                "id": "instagram",
                "placeholder": "@username",
            }),
        }