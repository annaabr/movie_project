from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.add_info, name='add_info'),
]