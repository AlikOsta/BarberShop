from . import models
from django import forms


class VisitForm(forms.ModelForm):
    class Meta:
        model = models.Visit
        fields = ['name', 'phone', 'comment', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}),
        }