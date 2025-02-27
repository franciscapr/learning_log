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
    # Pàgina para añadir un tema nuevo.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Pàgina para añadir una entrada nueva.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Pàgina para editar una entrada.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]