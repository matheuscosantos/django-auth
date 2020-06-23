from django.contrib import admin
from django.urls import path, include

import usuarios

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]
