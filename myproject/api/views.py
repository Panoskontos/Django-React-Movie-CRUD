from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
# Create your views here.
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # queue
        
        'Display product list':'products/',
        
        '         ':'           ',
    }

    return Response(api_urls)