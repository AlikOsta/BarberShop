from . import models
from django import forms


class VisitForm(forms.ModelForm):
    class Meta:
        model = models.Visit
        fields = ['name', 'phone', 'comment', 'master', 'services']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class VisitEditForm(forms.ModelForm):
    class Meta:
        model = models.Visit
        fields = ['name', 'phone', 'master', 'services', 'status', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-select'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }