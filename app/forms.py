from . import models
from django import forms
from captcha.fields import CaptchaField


class VisitForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=models.Service.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True
    )
    
    class Meta:
        model = models.Visit
        fields = ['name', 'phone', 'comment', 'master', 'services']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-select'}),
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


class ReviewForm(forms.ModelForm):
    captcha = CaptchaField(
        label='Подтвердите что вы человек'
    )
    
    class Meta:
        model = models.Review
        fields = ['author_name', 'text', 'photo', 'master', 'rating', 'captcha']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Напишите отзыв...(минимум 30 символов)'
            }),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.HiddenInput()
        }