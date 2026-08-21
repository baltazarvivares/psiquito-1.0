from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
     path('', views.Login, name='login'),
    path('register/', views.Register, name='register'),
]