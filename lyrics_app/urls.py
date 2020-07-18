
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), # admin page
    path('',include('lern_by.urls')) # moving to lern_by/urls.py to main page
]
