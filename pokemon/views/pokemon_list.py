from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from pokemon.models import Pokemon


@login_required
def user_pokemon_list(request):
    pokemons = Pokemon.objects.filter(user=request.user)
    return render(request, 'pokemon/pokemon_list.html', {'pokemons': pokemons})


@cache_page(60 * 60 * 24 * 30)
def pokemon_list(request):
    pokemons = Pokemon.objects.only('name', 'slug', 'number', 'image', 'user').select_related('user').prefetch_related('categories').all()

    page_number = request.GET.get('page') or 1
    per_page = request.GET.get('per_page') or 24
    paginator = Paginator(pokemons, per_page=per_page)

    query_dict = request.GET.copy()
    query_dict.pop('page', None)
    query_dict['per_page'] = per_page
    url_param = query_dict.urlencode()
    # request.path = http://127.0.0.1:8000/pokemon/
    # ?page=1&per_page=10&category=fire&search=test
    paginator_url = request.path + '?' + url_param
    query_dict.pop('per_page', None)
    url_param = query_dict.urlencode()
    per_page_url = request.path + ('?' + url_param + '&') if url_param else '?'
    
    page = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page.number, on_each_side=2, on_ends=1)
    return render(request, 'pokemon/pokemon_list.html', {
        'paginator': paginator,
        'page': page,
        'page_range': page_range,
        'paginator_url': paginator_url,
        'per_page_url': per_page_url,
    })
