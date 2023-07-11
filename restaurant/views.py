from rest_framework import generics
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework.viewsets import ModelViewSet

class MenuItemView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BookingViewSet(ModelViewSet):
    queryset = Booking,objects.all()
    serializer_class = BookingSerializer

    


    