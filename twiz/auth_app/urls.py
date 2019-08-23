from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'auth_app'
urlpatterns = [
    path('', views.auth_home, name = 'auth_home'),
    
]