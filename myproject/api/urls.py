from django.urls import path
from .views import *

urlpatterns = [
     path('', apiOverview, name='overview'),
    path('products', product_list, name='product_list')
]