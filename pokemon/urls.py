
"""
Dobré příklady:

/pokemons/
/pokemons/add/
/pokemons/pikachu/
/pokemons/pokachu/remove/
/pokemons/pikachu/update/

/cars/
/cars/add/
/cars/my-car/
/cars/my-car/remove/
/cars/my-car/update/


list
/

detail
/darek/10202/
/darek/10202/vonna-svicka/
/darek/vonna-svicka-10202/

/darek/list/ - moje darky
/darek/add/ - nový dárek
/darek/10202/edit/ - editace (zobrazení i uložení)
/darek/10202/delete/ - mazání


youtube.com/
youtube.com/feed/subscriptions/
youtube.com/watch?v=87JKAIUSD87

--------------------------------------------------

List Of Pokemons
/

Detail Of Pokemon
/23/
/pikachu/

Cantact Page
/contact/

About Page
/about/

"""

from django.urls import path
from django.shortcuts import HttpResponse


def test_view(request, **kwargs):
    print(kwargs)
    return HttpResponse('test page: ' + request.path)


"""
čím konkrétnější url cesta tím by měla být více nahoře
čím více dynamická, více dole
"""

urlpatterns = [
    path('', test_view),
    path('about/', test_view),
    path('contact/', test_view),
    path('pokemon/<int:number>/', test_view),
    path('pokemon/<slug:slug>/', test_view),
]
