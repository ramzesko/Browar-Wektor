import itertools
from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone


def recipes_list(request):
    recipes = Recipe.objects.filter(brew_date__lte=timezone.now()).order_by('-brew_date')
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    mass1 = [elem.weight for elem in Zasyp.objects.filter(recipe_id=pk)]
    mass2 = [elem.weight for elem in Chmielenie.objects.filter(recipe_id=pk)]
    mass1.sort(reverse=True)
    mass2.sort(reverse=True)
    ingredients=list(itertools.zip_longest(recipe.malts.all().order_by('-zasyp__weight'),mass1,
                                           recipe.hops.all().order_by('-chmielenie__weight'),mass2,
                                           recipe.other.all(),recipe.yeast.all(), fillvalue=''))
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients':ingredients})

def show_index(request):
    return render(request, 'index.html', {})

