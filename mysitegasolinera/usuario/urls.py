from django.urls import path
from . import views

urlpatterns = [
    path('form-usuario/', views.usuario)
]