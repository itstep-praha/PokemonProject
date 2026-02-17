from django.urls import path
from django.shortcuts import HttpResponse
from pokemon import views


def test_view(request, **kwargs):
    print(kwargs)
    return HttpResponse('test page: ' + request.path)


urlpatterns = [
    path('', views.index_view),
    path('pokemon/', views.pokemon_list),

    path('pokemon/create/', views.pokemon_create_view),
    path('pokemon/update/<int:pokemon_id>/', views.pokemon_update_view),

    path('pokemon/user/', views.user_pokemon_list),
    path('pokemon/<slug:pokemon_slug>/', views.pokemon_detail),

    path('pokemon/<int:pokemon_id>/comment/', views.create_comment), # pokemon_detail_number

    path('pokemon/<int:number>/', test_view), # pokemon_detail_number
    path('about/', test_view), # about_view
    path('contact/', test_view), # contact_view
    
    path('accounts/profile/', views.profile_view),
]
