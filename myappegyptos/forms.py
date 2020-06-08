from django import forms
from .models import Ville
from .models import Joueur

class VilleForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = ['name','description','imgVille','price']

class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['name','description','imgJoueur','club','pays']