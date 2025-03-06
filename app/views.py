from django.shortcuts import render

MENU = [
    {'title': 'Главная', 'url': '/', 'active': True},
    {'title': 'Мастера', 'url': '#masters', 'active': True},
    {'title': 'Услуги', 'url': '#services', 'active': True},
    # {'title': 'Отзывы', 'url': '#reviews', 'active': True},
    # {'title': 'Оставить отзыв', 'url': 'review/create', 'active': True},
    {'title': 'Записаться на стрижку', 'url': '#orderForms', 'active': True},
]
