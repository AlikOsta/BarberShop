from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q

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


class VisitListView(UserPassesTestMixin, ListView):
    model = Visit
    template_name = 'app/visit_list.html'
    context_object_name = 'visits'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        queryset = Visit.objects.all().order_by('-created_at')
        search_query = self.request.GET.get('q', '')
        status = self.request.GET.get('status', '')
        master_id = self.request.GET.get('master', '')

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(phone__icontains=search_query))
        if status:
            queryset = queryset.filter(status=status)
        if master_id:
            queryset = queryset.filter(master_id=master_id)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Visit.STATUS_CHOICES
        context['masters'] = Master.objects.all()
        context['search_query'] = self.request.GET.get('q', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['current_master'] = self.request.GET.get('master', '')
        return context
    
    def post(self, request):
        visit_id = request.POST.get('visit_id')
        new_status = request.POST.get('status')
        if visit_id and new_status:
            Visit.objects.filter(id=visit_id).update(status=new_status)
        return redirect('app:visit_list')


