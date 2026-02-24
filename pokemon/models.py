from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Django DB ORM
# Django
# DB - databáze
# ORM - Object Relation Mapper


class Pokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(blank=True, null=True, upload_to='pokemon_images/')
    number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    categories = models.ManyToManyField('Category', blank=True)
    create_dt = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.name
    
    @property
    def bootstrap_color(self):
        try:
            return category_to_bootstrap_color[self.slug]
        except KeyError:
            return 'secondary'


category_to_bootstrap_color = {
    'grass': 'success',
    'fire': 'danger',
    'water': 'info',
    'electric': 'warning',
    'poison': 'secondary',
    'ground': 'secondary',
    'rock': 'secondary',
    'bug': 'success',
    'ghost': 'dark',
    'steel': 'secondary',
    'dragon': 'primary',
    'psychic': 'danger',
    'ice': 'info',
    'fighting': 'danger',
    'fairy': 'info',
    'normal': 'secondary',
    'flying': 'info',
}


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # pokemon.comment_set.all() nebo nastavím related_name='comments' tak pokemon.comments.all()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']
