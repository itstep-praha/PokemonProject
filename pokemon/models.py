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
    name = models.CharField(max_length=50, verbose_name='Název 1')
    slug = models.SlugField(max_length=50, unique=True)
    categories = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    create_dt = models.DateTimeField(auto_now_add=True)
