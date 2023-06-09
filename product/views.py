from product.models import Category, Product, Review
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from product.serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    RatingSerializer,
)



@api_view(['GET', 'POST'])
def category_list_create_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        data = CategorySerializer(category, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data

        category = Category.objects.create(
            id=data.get('id'),
            name=data.get('name')
        )
        return Response(data=CategorySerializer(category, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_retrieve_update_delete_api_view(request, **kwargs):
    category = Category.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = CategorySerializer(category, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        category.id = data.get('id')
        category.name = data.get('name')

        category.save()
        return Response(data=CategorySerializer(category, many=False).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        data = request.data
        category.id = data.get('id')
        category.delete()
        return Response(data=CategorySerializer(category, many=False).data, status=status.HTTP_200_OK)

@api_view(['GET'])
def products_reviews_rating_view(request):
    products = Product.objects.all()
    serializer = RatingSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        data = ProductSerializer(product, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data

        product = Product.objects.create(
            id=data.get('id'),
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
        )
        product.category.set(data.get('category'))

        product.save()
        return Response(data=CategorySerializer(product, many=False).data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def product_retrieve_update_delete_api_view(request, **kwargs):
    product = Product.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = ProductSerializer(product, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        product.id = data.get('id')
        product.title = data.get('title')
        product.description = data.get('description')
        product.price = data.get('price')

        product.category.set(data.get('category'))
        product.save()
        return Response(data=ProductSerializer(product, many=False).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        data = request.data
        product.id = data.get('id')
        product.delete()
        return Response(data=ProductSerializer(product, many=False).data, status=status.HTTP_200_OK)




@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data

        review = Review.objects.create(
            id=data.get('id'),
            text=data.get('text'),
            stars=data.get('stars'),
        )
        review.product.set(data.get('product'))

        review.save()
        return Response(data=ReviewSerializer(review, many=False).data, status=status.HTTP_201_CREATED)




@api_view(['GET', 'PUT', 'DELETE'])
def review_retrieve_update_delete_api_view(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        review.id = data.get('id')
        review.text = data.get('text')
        review.stars = data.get('stars')

        review.product.set(data.get('product'))
        review.save()
        return Response(data=ProductSerializer(review, many=False).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        data = request.data
        review.id = data.get('id')
        review.delete()
        return Response(data=ProductSerializer(review, many=False).data, status=status.HTTP_200_OK)