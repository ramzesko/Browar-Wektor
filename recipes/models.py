from django.db import models

class Ingredient(models.Model):
    #kinds =(
    #    ('malt','słód'),('grain','surowiec niesłodowany'),('hop','chmiel'),('other','dodatek')
    #)
    #category = models.CharField(max_length=5, choices=kinds, null=True, blank=True)
    variety = models.CharField(max_length=50)
    #weight = models.FloatField(null=True, blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        return self.variety

class Malt(Ingredient):
    pass
class Hop(Ingredient):
    pass
class Other(Ingredient):
    pass
class Yeast(Ingredient):
    pass

class Recipe(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    style = models.CharField(max_length=100)
    OG = models.FloatField(default=0)
    ABV = models.FloatField(default=0)
    IBU = models.IntegerField(default=0)
    text = models.TextField()
    brew_date = models.DateField()
    bottled_date = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to="static/pictures/", blank=True)
    malts = models.ManyToManyField(Malt, through='Zasyp')
    hops = models.ManyToManyField(Hop, through='Chmielenie')
    other = models.ManyToManyField(Other, through='Dodatki')
    yeast = models.ManyToManyField(Yeast, through='Drożdże')

    def publish(self):
        self.save()
    def __str__(self):
        return self.title

class Zasyp(models.Model):
    malt = models.ForeignKey(Malt, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
class Chmielenie(models.Model):
    hop = models.ForeignKey(Hop,on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)

class Dodatki(models.Model):
    other = models.ForeignKey(Other,on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
class Drożdże(models.Model):
    kinds=(('starter płynne','starter płynne'),('suche','suche'),('gęstwa','gęstwa'))
    yeast = models.ForeignKey(Yeast,on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=kinds, null=True, blank=True)

