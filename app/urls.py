
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('masters/', views.MasterListView.as_view(), name='master_list'),
    path('masters/<int:pk>/', views.MasterDetailView.as_view(), name='master_detail'),
    path('visits/', views.VisitListView.as_view(), name='visit_list'),
    path('visits/<int:pk>/', views.VisitDetailView.as_view(), name='visit_detail'),
    path('visits/<int:pk>/edit/', views.VisitEditView.as_view(), name='visit_edit'),
    path('visits/<int:pk>/delete/', views.VisitDeleteView.as_view(), name='visit_delete'),
    path('get-services/', views.ServicesByMasterView.as_view(), name='get_services'),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    