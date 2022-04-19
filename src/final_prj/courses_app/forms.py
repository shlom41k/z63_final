from django import forms

from .models import SchoolCourseApplication
# from phone_field import PhoneField


class SchoolCourseApplicationForm(forms.ModelForm):
    class Meta:
        model = SchoolCourseApplication
        fields = ['course', 'user_name', 'phone', 'telegram']
        widgets = {
            "user_name": forms.TextInput(attrs={
                "label": "User Name",
                "class": "form-control",
                "id": "user_name",
                "placeholder": "Введите ваше имя",
                "required": "required",
            }),
            "phone": forms.TextInput(attrs={
                "label": "Last name",
                "class": "form-control",
                "id": "phone",
                "placeholder": "Введите номер Вашего телефона",
                "required": "required",
            }),
            "telegram": forms.TextInput(attrs={
                "label": "Telegram (если есть)",
                "class": "form-control",
                "id": "telegram",
                "placeholder": "(если есть) @bumblebeeschool",
            }),
        }
