from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from pokemon.models import Pokemon


@login_required
def user_pokemon_list(request):
    pokemons = Pokemon.objects.filter(user=request.user)
    return render_pokemon_list(request, pokemons, 'My Pokemons')


@cache_page(60 * 60 * 24 * 30)
def pokemon_list(request):
    pokemons = Pokemon.objects.only('name', 'slug', 'number', 'image', 'user').select_related('user').prefetch_related('categories').all()
    return render_pokemon_list(request, pokemons, 'Pokemon List')
    

def render_pokemon_list(request, queryset, title):
    page_number = request.GET.get('page') or 1
    per_page = request.GET.get('per_page') or 24
    paginator = Paginator(queryset, per_page=per_page)
    
    page = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page.number, on_each_side=2, on_ends=1)

    return render(request, 'pokemon/pokemon_list.html', {
        'title': title,
        'paginator': paginator,
        'page': page,
        'page_range': page_range,
        'paginator_url': get_paginator_url(request.path, request.GET, per_page),
        'per_page_url': get_per_page_url(request.path, request.GET),
    })


def get_paginator_url(path, query_dict, per_page):
    """ vrátí url pro paginator """
    query_dict = query_dict.copy()
    query_dict.pop('page', None)
    query_dict['per_page'] = per_page
    url_param = query_dict.urlencode()
    return path + '?' + ((url_param + '&') if url_param else '')


def get_per_page_url(path, query_dict):
    """ vrátí url pro per_page """
    query_dict = query_dict.copy()
    query_dict.pop('page', None)
    query_dict.pop('per_page', None)
    url_param = query_dict.urlencode()
    return path + '?' + ((url_param + '&') if url_param else '')
