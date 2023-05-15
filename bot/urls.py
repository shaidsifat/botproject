# scraper/urls.py

from django import views
from django.urls import path
from .views import search_products, update_products,search1
from . import views
urlpatterns = [
    path('search_products/', search_products, name='search_products'),
    path('update/', update_products, name='update_products'),
    path('search/', views.search1, name='search'),

]