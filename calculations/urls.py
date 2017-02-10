from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^calculations/carbonation/$', views.carbonation_calc, name='carbonation'),
    # url(r'^calculations/carbonation_result/$', views.carbonation, name='carbonation_result')
]