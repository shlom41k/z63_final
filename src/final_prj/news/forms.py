from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField

from .models import Comment, CommentAnswer, Post


class CommentForm(forms.ModelForm):
    """
    Form for creating a comment
    """
    class Meta:
        model = Comment
        fields = ("text", )
        widgets = {
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "cols": 40,
            }),
        }


class CommentAnswerForm(forms.ModelForm):
    """
    Form for creating a comment answer
    """
    class Meta:
        model = CommentAnswer
        fields = ("text", )
        widgets = {
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 1,
            }),
        }


class PostCreateForm(forms.ModelForm):
    """
    Form for creating a post
    """
    class Meta:
        model = Post
        fields = ("header_h1", "title", "description", "content", "image", "tag", )
        widgets = {
            "header_h1": forms.Textarea(attrs={
                "rows": 1,
                "label": "Post Header",
                "class": "form-control",
                "id": "header_h1",
                "placeholder": "Введите заголовок новости",
                "required": "required",
            }),
            "title": forms.Textarea(attrs={
                "rows": 1,
                "label": "Post Title",
                "class": "form-control",
                "id": "title",
                "placeholder": "Введите название новости",
                "required": "required",
            }),
            "description": RichTextUploadingFormField(label_suffix="1"),
            "content": RichTextUploadingFormField(),
            "image": forms.FileInput(attrs={
                "label": "Post Image",
                "class": "form-control",
                "id": "image",
                "placeholder": "Выберите изображение для новости",
                "required": "required",
            }),
            "tag": forms.TextInput(attrs={
                "label": "Post Tags",
                "class": "form-control",
                "id": "tag",
                "placeholder": "Введите теги новости",
                "required": "required",
            }),
        }

