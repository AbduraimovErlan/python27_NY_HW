from rest_framework import serializers
from product.models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class CategoryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ReviewRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'