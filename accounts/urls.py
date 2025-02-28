""" Define patrones de URL para accounts. """
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Incluye url autenticadas predeterminadas.
    path('', include('django.contrib.auth.urls')),
    # Pàgina de registro.
    path('register/', views.register, name='register'),
]
