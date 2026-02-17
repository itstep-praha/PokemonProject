# context processory přidávají data do všech templates
from functools import lru_cache
from pokemon.models import Category

def base(request):
    return {
        'nav_items': nav_items,
        'categories': get_categories(),
    }


nav_items = [
    {'text': 'All Pokemons', 'url': '/pokemon/'},
    {'text': 'Create Pokemons', 'url': '/pokemon/create/'},
    {'text': 'My Pokemons', 'url': '/pokemon/user/'},
    {'text': 'My Account', 'url': '/accounts/profile/'},
]


@lru_cache
def get_categories():
    # poznámka: na globální úrovni by neměly bát dotazy do db
    return Category.objects.all()
