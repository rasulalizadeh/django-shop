from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import models
from . import serializers


# Create your views here.
class ProductApi(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [AllowAny]


def index(request):
    products = [1,2,3,4,5,6,7,8,9,10]
    return render(request, 'index.html', {"products": products})
