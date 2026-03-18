from django.urls import path
from pokemon import views


urlpatterns = [
    path('', views.index_view, name='pokemon_index'),
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
    path('pokemon/user/', views.user_pokemon_list, name='user_pokemon_list'),
    path('pokemon/create/', views.pokemon_create_view, name='pokemon_create_view'),
    path('pokemon/<slug:pokemon_slug>/update/', views.pokemon_update_view, name='pokemon_update_view'),
    path('pokemon/<slug:pokemon_slug>/', views.pokemon_detail, name='pokemon_detail'),
    path('pokemon/<slug:pokemon_slug>/comment/', views.create_comment, name='pokemon_create_comment'),

    path('accounts/profile/', views.profile_view, name='profile_view'),

    path('example/pokemon/ajax/', views.pokemon_list_ajax, name='pokemon_list_ajax'),
    path('example/pokemon/json-data/', views.pokemon_list_json, name='pokemon_list_json'),
    path('example/pokemon/htmx/', views.pokemon_list_htmx, name='pokemon_list_htmx'),
    path('example/pokemon/htmx-part/', views.pokemon_part_htmx, name='pokemon_part_htmx'),
]
