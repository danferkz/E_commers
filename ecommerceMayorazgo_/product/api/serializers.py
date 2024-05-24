from rest_framework import serializers
from product.models import Products, Categories


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product_id', 'name', 'price', 'stock', 'image', 'description', 'proveedor', 'price_type']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'