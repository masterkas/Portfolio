from .models import Articles
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput, ImageField, EmailField


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'image', 'full_text','name', 'email', 'tel']

        widgets = {
            "title": TextInput(attrs={'class': "form-control", 'placeholder': "Название объявления"}),
            "anons": TextInput(attrs={'class': "form-control", 'placeholder': "О чем"}),
            "date": DateTimeInput(attrs={'class': "form-control", 'placeholder': "Дата публикации"}),
            "full_text": Textarea(attrs={'class': "form-control", 'placeholder': "Текст объявления"}),
            "name": TextInput(attrs={'class': "form-control", 'placeholder': "Имя"}),
            "tel": TextInput(attrs={'class': "form-control", 'placeholder': "Телефон"}),

        }