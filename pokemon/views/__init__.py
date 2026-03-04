from pokemon.views.pages import index_view, profile_view
from pokemon.views.pokemon_detail import pokemon_detail
from pokemon.views.pokemon_list import user_pokemon_list, pokemon_list
from pokemon.views.pokemon_edit import (
    pokemon_create_view,
    pokemon_update_view,
    create_comment,
)
from pokemon.views.examples import (
    pokemon_list_ajax,
    pokemon_list_htmx,
    pokemon_list_json,
    pokemon_part_htmx,
)