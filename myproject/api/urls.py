from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name='overview'),
    path('products', product_list, name='product_list'),
    path('products', create_product, name='create-product'),
    path('products/<str:pk>', update_product, name='update_product'),
    path('products/<str:pk>', delete_product, name='delete_product'),
    # Movies
    path('movies', movie_list),
    path('movies', create_movie),
    path('movies/<str:pk>', update_movie),
    path('movies/<str:pk>', delete_movie),
]