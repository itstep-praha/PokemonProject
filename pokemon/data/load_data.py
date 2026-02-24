import requests
from functools import lru_cache
from django.core.files.base import ContentFile
from django.utils.text import slugify
from pokemon.models import Pokemon, Category


def main():
    for num in range(1, 152):
        load_pokemon(num)


def load_pokemon(num):
    url = f'https://pokeapi.co/api/v2/pokemon/{num}/'
    data = requests.get(url).json()

    pokemon, _ = Pokemon.objects.update_or_create(
        number=num,
        slug=slugify(data['name']),
        defaults=dict(user_id=1, name=data['name'])
    )

    print('created:', pokemon)

    for item in data['types']:
        category = get_category(item['type']['name'])
        pokemon.categories.add(category)
    
    if not pokemon.image:
        image_url = data['sprites']['other']['official-artwork']['front_default']
        save_image_from_url(pokemon, image_url)


@lru_cache
def get_category(name):
    category, _ = Category.objects.update_or_create(
        slug=slugify(name),
        defaults=dict(name=name)
    )
    return category


def save_image_from_url(pokemon: Pokemon, url):
    response = requests.get(url)
    file_name = pokemon.slug + '-' + url.split("/")[-1]
    pokemon.image.save(file_name, ContentFile(response.content), save=True)


if __name__ == '__main__':
    main()

