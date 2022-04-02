from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name='overview'),
    path('products', product_list, name='product_list'),
    path('create-product', create_product, name='create-product'),
    path('read-product/<str:pk>', read_product, name='read_product'),
    path('update-product/<str:pk>', update_product, name='update_product'),
    path('delete-product/<str:pk>', delete_product, name='delete_product'),
]