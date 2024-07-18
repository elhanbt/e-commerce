from django.contrib import admin
from django.urls import path, include
from .views import index, products, singlepage, sample


urlpatterns = [
    path('bycart', index, name='index'),
    path('search/<str:value>/', products, name='search'),
    path('singlepage/<str:value>/', singlepage, name='singlepage'), 
    path('sample', sample, name = 'sample'),
]