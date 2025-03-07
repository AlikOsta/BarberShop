from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView
from .forms import VisitForm
from .models import Master, Service, Visit


class ThanksView(TemplateView):
    template_name = 'app/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(CreateView):
    template_name = 'app/main.html'
    form_class = VisitForm
    success_url = '/thanks/'
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = Master.objects.all()
        context['services'] = Service.objects.all()
        return context
    
