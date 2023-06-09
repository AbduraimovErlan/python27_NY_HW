from rest_framework import serializers
from product.models import Category, Product, Review


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'product_name', 'text',  'stars')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'category')



class ProductSerializer(serializers.ModelSerializer):
    list_review = ReviewSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'category_name', 'title', 'description', 'price', 'category',  'list_review')



