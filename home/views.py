from django.shortcuts import render, get_object_or_404, redirect
from .models import Recurso
from .permissions import tiene_permiso

def listar_recursos(request):
    recursos = Recurso.objects.all()
    return render(request, 'recursos/listar_recursos.html', {'recursos': recursos})

def crear_recurso(request):
    # Lógica para crear un nuevo recurso
    pass

def modificar_recurso(request, recurso_id):
    # Lógica para modificar un recurso existente
    pass

def eliminar_recurso(request, recurso_id):
    # Lógica para eliminar un recurso existente
    pass
