from django import forms
from .models import Pais, Departamento, Municipio #crear los formularios


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre', 'codigo']


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'codigo']
        

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombre', 'codigo']
