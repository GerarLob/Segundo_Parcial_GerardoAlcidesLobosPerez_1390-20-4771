from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_recursos, name='listar_recursos'),
    path('crear/', views.crear_recurso, name='crear_recurso'),
    path('modificar/<int:recurso_id>/', views.modificar_recurso, name='modificar_recurso'),
    path('eliminar/<int:recurso_id>/', views.eliminar_recurso, name='eliminar_recurso'),
]
