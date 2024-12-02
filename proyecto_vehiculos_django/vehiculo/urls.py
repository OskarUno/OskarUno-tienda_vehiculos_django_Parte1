from django.urls import path
from . import views

app_name = 'vehiculo'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('list/', views.listar, name='listar'),
]
