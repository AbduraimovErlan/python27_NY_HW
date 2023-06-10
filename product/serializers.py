from rest_framework import serializers
from product.models import Category, Product, Review


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'rating')


class ReviewSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.title', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'product_name', 'text', 'stars', 'product')


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(source='products.count', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products_count')


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'description', 'price', 'reviews')
