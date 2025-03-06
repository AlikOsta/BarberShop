
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    
    ] 
    