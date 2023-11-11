from rest_framework import serializers
from .models import OrderPlaced, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'selling_price')


class OrderPlacedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    def get_status(self, instance):
        instance.status

    class Meta:
        model = OrderPlaced
        fields = ('id', 'user', 'product', 'quantity', 'ordered_date', 'status')

