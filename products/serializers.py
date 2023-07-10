from django.urls import reverse
from rest_framework import serializers

from products.models import Product
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField()
    category = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"