from django import forms
from django.core.exceptions import ValidationError

from .models import *

# class Add_postForm(forms.Form):
#     name = forms.CharField(max_length=255, label='Название:', widget=forms.TextInput(attrs={'placeholder': 'Введите название товара'}))
#     slug = forms.SlugField(max_length=255, label='URL:')
#     description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание:')
#     is_publishes = forms.BooleanField(label="Публикация", required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория:', empty_label='категория не выбрана')



class Add_postForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Components
        fields = ['name', 'slug', 'description', 'photo', 'tel', 'is_publishes', 'cat']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return name