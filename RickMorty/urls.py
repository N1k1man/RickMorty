from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('mainapp.urls')),
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/authtoken/', include('djoser.urls.authtoken')),
]
