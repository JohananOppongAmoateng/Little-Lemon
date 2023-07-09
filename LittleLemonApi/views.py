from django.shortcuts import render
from .models import Cart,Category,Order,OrderItem,MenuItem
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import MenuItemSerializer,CategorySerializer,CartSerializer,OrderSerializer,OrderItemSerializer
# from rest_framework.permissions import p

# Create your views here.

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class GetMenuItem(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# class 
    