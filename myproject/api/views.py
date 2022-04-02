from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializers import ProductSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # queue
        'Display product list':'products/',
        'Create View':'create-product/',
        'Detail View':'read-product/<str:pk>',
        'Update View':'update-product/<str:pk>',
        'Delete View':'delete-product/<str:pk>',
        
        '         ':'           ',
    }

    return Response(api_urls)

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)


@api_view(['GET'])
def read_product(request,pk):
    if request.method == 'GET':
        products = Product.objects.get(id=pk)
        # many=False means return 1 object
        products_serializer = ProductSerializer(products, many=False)
        return Response(products_serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 


@api_view(['POST'])
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    
    return Response('Product was deleted!') 
