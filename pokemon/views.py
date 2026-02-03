from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pokemon.models import Pokemon


def index_view(request):
    return render(request, 'pokemon/index.html')


def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html', {'moje_jmeno': 'Nějaká hodnota', 'pokemons': pokemons})


# @login_required
def pokemon_detail(request, pokemon_slug):
    return render(request, 'pokemon/pokemon_detail.html')
