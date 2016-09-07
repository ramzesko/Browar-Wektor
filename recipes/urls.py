from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^recipe/(?P<pk>[0-9]+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^recipes_list', views.recipes_list, name='recipes_list'),
]