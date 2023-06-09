from rest_framework import serializers
from product.models import Category, Product, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'product_name', 'text',  'stars', 'count_reviews')

        # fields = '__all__'
        # fields = 'id text stars'.split()

class ReviewRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ('id', 'name', 'category')

class CategoryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    list_review = ReviewSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'category_name', 'title', 'description', 'price', 'category',  'list_review')

class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


