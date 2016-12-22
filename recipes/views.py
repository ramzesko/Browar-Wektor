import itertools
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
#from .form import PostForm

def recipes_list(request):
    recipes = Recipe.objects.filter(brew_date__lte=timezone.now()).order_by('-brew_date')
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # malts_all = Malt.objects.all()
    # hops_all = Hop.objects.all()
    # other_all = Other.objects.all()
    # yeast_all = Yeast.objects.all()
    # malts = []
    # hops = []
    # others = []
    # yeasts = []
    #for malt,hop,other,yeast in itertools.zip_longest(malts_all,hops_all,other_all,yeast_all, fillvalue=Malt.objects.get(variety='-')):
    #for malt, hop, other, yeast in zip(malts_all, hops_all, other_all, yeast_all):
        #if recipe in malt.recipe_set.all():
        #    malts.append(malt)
        #else: malts.append('')
        #if recipe in hop.recipe_set.all():
        #    hops.append(hop)
        #else: hops.append('')
        #if recipe in other.recipe_set.all():
        #    others.append(other)
        #else: others.append('')
        #if recipe in yeast.recipe_set.all():
        #    yeasts.append(yeast)
        #else: yeasts.append('')
        #ingredients = list(itertools.zip_longest(malts, hops, others, yeasts, fillvalue=''))
    zasypy = Zasyp.objects.filter(recipe_id=pk)
    chmiele = Chmielenie.objects.filter(recipe_id=pk)
    mass1 = [elem.weight for elem in zasypy]
    mass2 = [elem.weight for elem in chmiele]
    ingredients=list(itertools.zip_longest(recipe.malts.all().order_by('-zasyp__weight'),mass1,recipe.hops.all().order_by('chmielenie__weight'),mass2,recipe.other.all(),recipe.yeast.all(), fillvalue=''))
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients':ingredients})
#def post_new(request):
#    if request.method=='POST':
#        form=PostForm(request.POST)
#        if form.is_valid():
#            post=form.save(commit=False)
#            post.author=request.user
#            post.published_date=timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form=PostForm()
#    return render(request,'blog/post_edit.html',{'form':form})
#def post_edit(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#        form = PostForm(request.POST, instance=post)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm(instance=post)
#    return render(request, 'blog/post_edit.html', {'form': form})
def show_index(request):
    return render(request, 'index.html', {})

