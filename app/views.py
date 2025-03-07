from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView, UpdateView, DeleteView
from .forms import VisitForm, VisitEditForm
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

    def get_queryset(self):
        queryset = Visit.objects.all().order_by('-created_at')
        search_query = self.request.GET.get('q', '')
        master_id = self.request.GET.get('master', '')
        status = self.request.GET.get('status', '')

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(phone__icontains=search_query))

        if master_id:
            queryset = queryset.filter(master_id=master_id)
        
        if status:
            queryset = queryset.filter(status=status)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = Master.objects.all()
        context['status_choices'] = Visit.STATUS_CHOICES
        context['search_query'] = self.request.GET.get('q', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['current_master'] = self.request.GET.get('master', '')
        return context
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('app:index')

    def post(self, request):
        visit_id = request.POST.get('visit_id')
        new_status = request.POST.get('status')
        if visit_id and new_status:
            Visit.objects.filter(id=visit_id).update(status=new_status)
        return redirect('app:visit_list')
    


class VisitDetailView(UserPassesTestMixin, DetailView):
    model = Visit
    template_name = 'app/visit_detail.html'
    context_object_name = 'visit'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('app:index')
    

class VisitEditView(UserPassesTestMixin, UpdateView):
    model = Visit
    form_class = VisitEditForm
    template_name = 'app/visit_edit.html'
    success_url = reverse_lazy('app:visit_list')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('app:index')
    

class VisitDeleteView(UserPassesTestMixin, DeleteView):
    model = Visit
    template_name = 'app/visit_delete.html'
    success_url = reverse_lazy('app:visit_list')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('app:index')
    

class ServicesByMasterView(View):
    def get(self, request):
        master_id = request.GET.get('master_id')
        if master_id:
            services = Service.objects.filter(masters__id=master_id).values('id', 'name', 'price')
            return JsonResponse(list(services), safe=False)
        return JsonResponse([], safe=False)