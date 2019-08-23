from . import views
from django.urls import path

app_name = 'twizzy'
urlpatterns = [
    path('', views.home, name = 'home'),
]