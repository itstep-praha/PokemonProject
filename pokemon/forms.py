from django import forms
from pokemon.models import Pokemon, Comment

"""
1. vykreslení formuláře
2. uživatel vyplní data
3. uživatel odešle formulář
4. server dostane data
5. server: kontrola dat
6. Form is Valid -> uloží záznam -> vrátí uživateli OK stránku
7. Form is Invalid -> vykreslení formuláře + zobrazení chyb

https://learndjango.com/tutorials/20-django-packages-i-use-every-project
"""

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['number', 'name', 'categories']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
