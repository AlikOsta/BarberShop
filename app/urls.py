
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('masters/', views.MasterListView.as_view(), name='master_list'),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    