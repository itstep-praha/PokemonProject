from django.urls import path
from pokemon import views


urlpatterns = [
    path('', views.index_view),
    path('pokemon/', views.pokemon_list),
    path('pokemon/user/', views.user_pokemon_list),
    path('pokemon/create/', views.pokemon_create_view),
    path('pokemon/<slug:pokemon_slug>/update/', views.pokemon_update_view),
    path('pokemon/<slug:pokemon_slug>/', views.pokemon_detail),
    path('pokemon/<slug:pokemon_slug>/comment/', views.create_comment),   

    path('accounts/profile/', views.profile_view),

    path('example/pokemon/ajax/', views.pokemon_list_ajax),
    path('example/pokemon/json-data/', views.pokemon_list_json),
    path('example/pokemon/htmx/', views.pokemon_list_htmx),
    path('example/pokemon/htmx-part/', views.pokemon_part_htmx),
]
