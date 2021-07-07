from django.db import models
from datetime import datetime


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    discount = models.DecimalField(max_digits=12, decimal_places=0)
    status = models.BooleanField()
    create_at = models.DateTimeField(default=datetime.now())
    update_at = models.DateTimeField(null=True)

    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT, null=True)
