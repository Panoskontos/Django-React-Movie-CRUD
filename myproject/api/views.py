from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializers import ProductSerializer, MovieSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view



# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         # queue
#         'Display product list':'products/',
#         'Create View':'products/',
#         'Update View':'update-product/<str:pk>',
#         'Delete View':'delete-product/<str:pk>',
#         'Display product list':'movies/',
#         'Create View':'movies/',
#         'Update View':'movies/<str:pk>',
#         'Delete View':'movies/<str:pk>',
#     }

#     return Response(api_urls)

# @api_view(['GET'])
# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         products_serializer = ProductSerializer(products, many=True)
#         return Response(products_serializer.data)

# @api_view(['POST'])
# def create_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

# @api_view(['GET'])
# def read_product(request,pk):
#     if request.method == 'GET':
#         products = Product.objects.get(id=pk)
#         # many=False means return 1 object
#         products_serializer = ProductSerializer(products, many=False)
#         return Response(products_serializer.data)




# @api_view(['PUT'])
# def update_product(request,pk):
#     product = Product.objects.get(id=pk)
#     serializer = ProductSerializer(instance=product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

# @api_view(['DELETE'])
# def delete_product(request,pk):
#     product = Product.objects.get(id=pk)
#     product.delete()
    
#     return Response('Product was deleted!') 


# #------------------------- movies---------------------------------

# @api_view(['GET'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         movies_serializer = MovieSerializer(movies, many=True)
#         return Response(movies_serializer.data)

# @api_view(['POST'])
# def create_movie(request):
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

# @api_view(['GET'])
# def read_movie(request,pk):
#     if request.method == 'GET':
#         products = Movie.objects.get(id=pk)
#         # many=False means return 1 object
#         products_serializer = MovieSerializer(products, many=False)
#         return Response(products_serializer.data)




# @api_view(['PUT'])
# def update_movie(request,pk):
#     product = Movie.objects.get(id=pk)
#     serializer = MovieSerializer(instance=product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

# @api_view(['DELETE'])
# def delete_movie(request,pk):
#     product = Movie.objects.get(id=pk)
#     product.delete()
    
#     return Response('movie was deleted!') 



# fastest api
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()