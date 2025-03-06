from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView

MENU = [
    {'title': 'Главная', 'url': '/', 'active': True},
    {'title': 'Мастера', 'url': '#masters', 'active': True},
    {'title': 'Услуги', 'url': '#services', 'active': True},
    # {'title': 'Отзывы', 'url': '#reviews', 'active': True},
    # {'title': 'Оставить отзыв', 'url': 'review/create', 'active': True},
    {'title': 'Записаться на стрижку', 'url': '#orderForms', 'active': True},
]


class ThanksView(TemplateView):
    template_name = 'app/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        return context



