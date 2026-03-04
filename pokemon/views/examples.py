from django.http import JsonResponse
from django.shortcuts import render
from pokemon.models import Pokemon


def pokemon_list_ajax(request):
    """ html page for ajax example """
    return render(request, 'pokemon/pokemon_list_ajax.html')


def pokemon_list_htmx(request):
    """ html page for htmx example """
    return render(request, 'pokemon/pokemon_list_htmx.html')


def pokemon_list_json(request):
    per_page = 30
    startFrom = int(request.GET.get('startFrom') or 0)
    until = startFrom + per_page

    data = Pokemon.objects.values('name', 'number')
    data = list(data[startFrom:until])

    if len(data) < per_page:
        next_url = None
    else:
        next_url = '/pokemon-json/?startFrom=' + str(until)

    return JsonResponse({
        'data': data,
        'next': next_url,
    })



def pokemon_part_htmx(request):
    per_page = 30
    startFrom = int(request.GET.get('startFrom') or 0)
    until = startFrom + per_page

    data = Pokemon.objects.all()
    data = list(data[startFrom:until])

    if len(data) < per_page:
        next_url = None
    else:
        next_url = '/pokemon-json/?startFrom=' + str(until)

    return render(request, 'pokemon/include/pokemon_list.html', {
        'object_list': data,
    })
