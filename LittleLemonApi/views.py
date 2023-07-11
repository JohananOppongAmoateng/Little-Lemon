from django.shortcuts import render
from .models import Cart,Category,Order,OrderItem,MenuItem
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .permissions import IsManagerOrReadOnly,IsManager
from .serializers import MenuItemSerializer,UserSerializer,CategorySerializer,CartSerializer,OrderSerializer,OrderItemSerializer


# Create your views here.

class MenuItemList(generics.ListCreateAPIView,):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated,IsManagerOrReadOnly]

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated,IsManagerOrReadOnly]

class Manager(generics.RetrieveDestroyAPIView):
    queryset = User.objects.filter(groups__name="Manager")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsManager]

class ListManager(generics.ListCreateAPIView):
    queryset =  User.objects.filter(groups__name="Manager")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsManager]


class AddDeliveryStaff(APIView):
    queryset =  User.objects.filter(groups__name="Delivery Crew")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsManager]
    

class DeliveryStaffs(generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset =  User.objects.filter(groups__name="Delivery Crew")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsManager]



class CartView(generics.RetrieveDestroyAPIView,generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user)
        return cart



class OrderView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user)
        return cart



    