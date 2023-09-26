from django import forms
from .models import Idolo, Experiencia

class IdoloForm(forms.ModelForm):
    class Meta:
        model = Idolo
        fields = ['player', 'titles_won', 'games', 'era', 'position']

class UpdateIdoloForm(forms.ModelForm):
    class Meta:
        model = Idolo
        fields = ['player', 'titles_won', 'games', 'era', 'position']

class DeleteIdoloForm(forms.ModelForm):
    class Meta:
        model = Idolo
        fields = []


class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['experiences', 'where', 'with_who', 'type']

class ExperienciaUpdateForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['experiences', 'where', 'with_who', 'type']

class ExperienciaDeleteForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = [] 