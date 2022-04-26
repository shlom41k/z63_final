from django import forms
from django.core.validators import EmailValidator


class FeedBackForm(forms.Form):
    """
    Form for feedback
    """
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
            'label': 'Name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': "Ваше имя",
        })
    )

    email = forms.CharField(
        max_length=100,
        label='Email',
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={
            'label': 'Email',
            'class': 'form-control',
            'id': 'email',
            'placeholder': "Ваша почта",
        })
    )

    subject = forms.CharField(
        max_length=200,
        label='Subject',
        widget=forms.TextInput(attrs={
            'label': 'Subject',
            'class': 'form-control',
            'id': 'subject',
            'placeholder': "Тема",
        })
    )

    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'label': 'Message',
            'class': 'form-control md-textarea',
            'id': 'message',
            'rows': 5,
            'placeholder': "Ваше сообщение",
        })
    )
