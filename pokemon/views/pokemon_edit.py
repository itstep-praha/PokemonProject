from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from pokemon.models import Pokemon
from pokemon.forms import PokemonForm, CommentForm


@login_required
def pokemon_create_view(request):
    if request.method == 'GET':
        form = PokemonForm()
    else:
        form = PokemonForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.slug = slugify(instance.name)
            instance.save()
            return redirect('/pokemon/user/')
        
    return render(request, 'pokemon/pokemon_form.html', {'form': form})


@login_required
def pokemon_update_view(request, pokemon_slug):
    pokemon = get_object_or_404(Pokemon, slug=pokemon_slug)

    if request.method == 'GET':
        form = PokemonForm(instance=pokemon)
    else:
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)

        if form.is_valid():
            instance = form.save()
            return redirect('/pokemon/user/')
        
    return render(request, 'pokemon/pokemon_form.html', {'form': form})


@login_required
def create_comment(request, pokemon_slug):
    pokemon = get_object_or_404(Pokemon, slug=pokemon_slug)

    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.pokemon = pokemon
        comment.user = request.user
        comment.save()

    return redirect(f'/pokemon/{pokemon.slug}/')
