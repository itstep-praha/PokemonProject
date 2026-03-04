from django.shortcuts import get_object_or_404, render
from pokemon.models import Pokemon
from pokemon.forms import CommentForm


def pokemon_detail(request, pokemon_slug):
    pokemon = get_object_or_404(Pokemon, slug=pokemon_slug)
    comment_form = CommentForm()
    return render(request, 'pokemon/pokemon_detail.html', {'pokemon': pokemon, 'comment_form': comment_form})
