from rest_framework import serializers
from . import models


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'name', 'price', 'discount', 'status']
