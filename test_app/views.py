import datetime as dt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from test_app.models import Student
from pokemon.models import Pokemon


def my_site_view(request):
    return HttpResponse('Hello')

def my_json_view(request):
    return JsonResponse({
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
    })

def my_template_view(request):
    return render(request, 'test_app/my_template.html', {
        'datum': dt.datetime.now(),
        'key': 'value',
        'data': DATA,
    })

DATA = [
    {'name': 'Suche', 'age': 20},
    {'name': 'Jana', 'age': 40},
    {'name': 'Petr', 'age': 30},
]

def my_name_view(request, name):
    for item in DATA:
        if item['name'] == name:
            return HttpResponse(str(item))
    
    return HttpResponse('not found', status=404)


def my_user_view(request, user_id):
    data = Student.objects.all()
    data = Pokemon.objects.values('pk', 'name')
    return JsonResponse(list(data), safe=False)
