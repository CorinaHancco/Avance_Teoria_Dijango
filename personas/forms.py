from django import forms
from .models import Persona

class PersonaForm(forms.Form):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'donador',
        ]
    
class RawPersonaForm(forms.Form):
    nombres = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Solo tu nombre, por favor',
                'id':'nombreID',
                'class':'special',
                'cols':'10',
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()