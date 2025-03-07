from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView
from .forms import VisitForm
from .models import Master, Service


class ThanksView(TemplateView):
    template_name = 'app/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(View):
    def get(self, request):
        context = {
            'masters': Master.objects.all(),
            'services': Service.objects.all(),
            'form': VisitForm(),
        }
        return render(request, 'app/main.html', context)
    
    def post(self, request):
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:thanks')
        
        context = {
            'masters': Master.objects.all(),
            'services': Service.objects.all(),
            'form': form,
        }
        return render(request, 'app/main.html', context)
    
