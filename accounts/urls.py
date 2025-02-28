""" Define patrones de URL para accounts. """
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Incluye url de autneticaciòn predeterminadas.
    path('', include('django.contrib.auth.urls')),
]