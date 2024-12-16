from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import welcome_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')), 
    path('', welcome_view, name='welcome'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)