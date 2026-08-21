from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('registro/', views.Registro, name='registro'),
]