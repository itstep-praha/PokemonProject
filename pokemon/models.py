from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Pokemon(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(blank=True, null=True, upload_to='pokemon_images/')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    categories = models.ManyToManyField('Category', blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)

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
    def color(self):
        return CATEGORY_COLOR[self.slug]


CATEGORY_COLOR = {
    "bug": {"bg": "#A8B820", "text": "#FFFFFF"},
    "dragon": {"bg": "#7038F8", "text": "#FFFFFF"},
    "electric": {"bg": "#F8D030", "text": "#000000"},
    "fairy": {"bg": "#EE99AC", "text": "#000000"},
    "fighting": {"bg": "#C03028", "text": "#FFFFFF"},
    "fire": {"bg": "#F08030", "text": "#FFFFFF"},
    "flying": {"bg": "#A890F0", "text": "#000000"},
    "ghost": {"bg": "#705898", "text": "#FFFFFF"},
    "grass": {"bg": "#78C850", "text": "#000000"},
    "ground": {"bg": "#E0C068", "text": "#000000"},
    "ice": {"bg": "#98D8D8", "text": "#000000"},
    "normal": {"bg": "#A8A878", "text": "#FFFFFF"},
    "poison": {"bg": "#A040A0", "text": "#FFFFFF"},
    "psychic": {"bg": "#F85888", "text": "#FFFFFF"},
    "rock": {"bg": "#B8A038", "text": "#FFFFFF"},
    "steel": {"bg": "#B8B8D0", "text": "#000000"},
    "water": {"bg": "#6890F0", "text": "#FFFFFF"}
}


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']
