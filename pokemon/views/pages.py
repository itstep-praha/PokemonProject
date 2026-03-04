from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required


@cache_page(60 * 60 * 24 * 30)
def index_view(request):
    return render(request, 'pokemon/index.html')


@login_required
def profile_view(request):
    return render(request, 'pokemon/profile.html')
