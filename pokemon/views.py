from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from pokemon.models import Pokemon
from pokemon.forms import PokemonForm, CommentForm


def index_view(request):
    return render(request, 'pokemon/index.html')


@login_required
def profile_view(request):
    return render(request, 'pokemon/profile.html')


@login_required
def pokemon_create_view(request):
    if request.method == 'GET':
        form = PokemonForm()
    else:
        form = PokemonForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False) # form.save() vrací instanci
            instance.user = request.user
            # zde se dají doplnit další atributy/fields pro instanaci
            instance.slug = slugify(instance.name)
            instance.save()
            print('instance.pk:', instance.pk)
            return redirect('/pokemon/user/') # redirect jestli to proběhlo v pořádku

    # template_name = '[nazev_app]/[nazev_modelu]_form.html'
    return render(request, 'pokemon/pokemon_form.html', {'form': form})


@login_required
def pokemon_update_view(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    if request.method == 'GET':
        form = PokemonForm(instance=pokemon)
    else:
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)

        if form.is_valid():
            instance = form.save()
            return redirect('/pokemon/user/')
        
    return render(request, 'pokemon/pokemon_form.html', {'form': form})


@login_required
def user_pokemon_list(request):
    if request.user.groups.filter(name='A1').exists():
        pokemons = Pokemon.objects.filter(user=request.user)
        return render(request, 'pokemon/pokemon_list.html', {'pokemons': pokemons})
    else:
        return HttpResponse('K této akci nemáte přístup')


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


def pokemon_detail(request, pokemon_slug):
    # pokemon = Pokemon.objects.get(pk=pk)
    pokemon = get_object_or_404(Pokemon, slug=pokemon_slug)
    comment_form = CommentForm()
    return render(request, 'pokemon/pokemon_detail.html', {'pokemon': pokemon, 'comment_form': comment_form})


# /pokemon/41/comment/

@login_required
def create_comment(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.pokemon_id = pokemon_id
        comment.user = request.user
        comment.save()

    return redirect(f'/pokemon/{pokemon.slug}/')


