from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView
from .forms import VisitForm
from .models import Master, Service, Visit


class ThanksView(TemplateView):
    template_name = 'app/thanks.html'


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
    

class MasterListView(ListView):
    model = Master
    template_name = 'app/master_list.html'
    context_object_name = 'masters'


class MasterDetailView(DetailView):
    model = Master
    template_name = 'app/master_detail.html'
    context_object_name = 'master'


