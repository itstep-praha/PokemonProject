import json
from django.utils.text import slugify
from pokemon.models import Category


def load():
    with open('pokemon/data/pokemon_categories.json') as file:
        data = json.load(file)
        for name in data["categories"]:
            slug = slugify(name)

            Category.objects.update_or_create(
                slug=slug, # unikátní klíč
                defaults={'name': name} # data, která se mohou měnit
            )
