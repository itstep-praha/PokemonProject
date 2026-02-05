from django.shortcuts import render, HttpResponse, redirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from pokemon.models import Pokemon
from pokemon.forms import PokemonForm


def index_view(request):
    return render(request, 'pokemon/index.html')


@login_required
def pokemon_create_view(request):
    if request.method == 'GET':
        form = PokemonForm()
    else:
        form = PokemonForm(request.POST)

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
def user_pokemon_list(request):
    if request.user.groups.filter(name='A1').exists():
        pokemons = Pokemon.objects.filter(user=request.user)
        return render(request, 'pokemon/pokemon_list.html', {'moje_jmeno': 'Nějaká hodnota', 'pokemons': pokemons})
    else:
        return HttpResponse('K této akci nemáte přístup')


def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html', {'moje_jmeno': 'Nějaká hodnota', 'pokemons': pokemons})


# @login_required
def pokemon_detail(request, pokemon_slug):
    return render(request, 'pokemon/pokemon_detail.html')
