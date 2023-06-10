from rest_framework import serializers
from .models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


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
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        # fields = ('id', 'category', 'title', 'description', 'price', 'reviews')
        fields = '__all__'

""" validate """

class ValidateProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(min_value=0, max_value=255)
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())

    def validate_tag(self, tags):
        filtered_tags = Tag.objects.filter(id__in=tags)
        if len(tags) == filtered_tags.count():
            return tags

        lst_ = {i['id'] for i in filtered_tags.values_list().values()}

        raise ValidationError(f'This ids doesnt exist {set(tags).difference(lst_)}')

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError(f"Error! {category_id} does not exists")
        return category_id

class ValidateCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

class ValidateReviewSerializer(serializers.Serializer):
    text = serializers.Serializer(required=False)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Review.objects.get(product_id=product_id)
        except Review.DoesNotExist:
            raise ValidationError('Review doesnt exist')