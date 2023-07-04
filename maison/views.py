from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets, filters
from .serializers import *
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response

# Create your views here.

class houseView(viewsets.ModelViewSet):
 
    serializer_class = houseSerializer
    queryset = House.objects.all()
class ListHouseView(ListAPIView):
    # queryset= House.objects.all()
    serializer_class= houseSerializer
    def get_queryset(self):
        return House.objects.order_by('-views')

class CreateHouseView(CreateAPIView):
    queryset= House.objects.all()
    serializer_class= houseSerializer
class searchHouseView(ListAPIView):
    queryset = House.objects.all()
    serializer_class = houseSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category'] 
    name = 'house-list'
    search_fields = (
        'category',
        'price',
        'Nom_proprio',
        'quartier',
        'isNegociable',
    )   
class UpdateHouseView(UpdateAPIView): 
    queryset= House.objects.all()
    serializer_class= houseSerializer

class DeleteHouseView(DestroyAPIView):
    queryset= House.objects.all()
    serializer_class= houseSerializer
    
    
class meubleView(viewsets.ModelViewSet):
 
    serializer_class = meublesSerializer
    queryset = meubles.objects.all()
class ListMeubleView(ListAPIView):
    # queryset= meubles.objects.all()
    def get_queryset(self):
        return meubles.objects.order_by('-views')
    serializer_class= meublesSerializer
class searchMeubleView(ListAPIView):
    queryset = meubles.objects.all()
    serializer_class = meublesSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category'] 
    name = 'meuble-list'
    search_fields = (
        'category',
        'price',
        'Nom_proprio',
        'quartier',
        'isNegociable',
    ) 
class CreateMeubleView(CreateAPIView):
    queryset= meubles.objects.all()
    serializer_class= meublesSerializer
    
class UpdateMeubleView(UpdateAPIView): 
    queryset= meubles.objects.all()
    serializer_class= meublesSerializer

class DeleteMeubleView(DestroyAPIView):
    queryset= meubles.objects.all()
    serializer_class= meublesSerializer    