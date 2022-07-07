from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.index, name = 'home'),
    path('fitness/', views.fitness, name = 'fitness'),
    path('martial-arts/', views.martial, name = 'martial-arts'),
    path('aquatics/', views.aquatics, name = 'aquatics'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('search/', views.search, name='search'),
    path('search/products', views.products, name='products'),

]
