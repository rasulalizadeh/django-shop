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
    return render(request, 'index.html')
