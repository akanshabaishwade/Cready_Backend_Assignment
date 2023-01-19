from django.urls import re_path as url, include
from django.contrib import admin
from django.urls import path



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('app_1.urls')),
]