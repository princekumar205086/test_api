from django.contrib import admin
from django.urls import path, include
from myapp.views import welcome_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')), 
    path('', welcome_view, name='welcome'),  
]