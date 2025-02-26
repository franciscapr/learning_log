"""Define patrones de URL para learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Pàgina de inicio
    path('', views.index, name='index'),
    # Pàgina que muestra todos los temas.
    path('topics/', views.topics, name='topics'),
    # Pàgina de detalle sobre un tema individual.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]