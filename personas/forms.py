from django import forms
from .models import Persona

class PersonaForm(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.ImageField()
    donador = forms.BooleanField()
    