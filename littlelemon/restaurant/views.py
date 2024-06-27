from django.shortcuts import render
from .models import Menu
from .serializers import MenuSerializer

from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, "index.html", {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer