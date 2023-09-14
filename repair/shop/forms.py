from django import forms
from .models import Usluga


class UslugaForm(forms.ModelForm):
    class Meta:
        model = Usluga
        fields = ['title', 'author', 'description', 'image', 'genre','cost']