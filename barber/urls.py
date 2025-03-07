
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

handler404 = 'app.views.custom_404'

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('app.urls')),
    ] 
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)