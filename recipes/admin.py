from django.contrib import admin

from .models import Recipe,Malt,Hop,Other,Yeast,Zasyp,Chmielenie,Dodatki,Drożdże

class ZasypInline(admin.TabularInline):
    model = Zasyp
    extra = 1
class ChmielenieInline(admin.TabularInline):
    model = Chmielenie
    extra = 1
class DodatkiInline(admin.TabularInline):
    model = Dodatki
    extra = 1
class DrożdżeInline(admin.TabularInline):
    model = Drożdże
    extra = 1
class MaltAdmin(admin.ModelAdmin):
    inlines = (ZasypInline,)
class HopAdmin(admin.ModelAdmin):
    inlines = (ChmielenieInline,)
class OtherAdmin(admin.ModelAdmin):
    inlines = (DodatkiInline,)
class YeastAdmin(admin.ModelAdmin):
    inlines = (DrożdżeInline,)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (ZasypInline,ChmielenieInline,DodatkiInline,DrożdżeInline)

admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Malt,MaltAdmin)
admin.site.register(Hop,HopAdmin)
admin.site.register(Other,OtherAdmin)
admin.site.register(Yeast, YeastAdmin)