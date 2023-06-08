from product.models import Category, Product, Review
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from product.serializers import (
    CategorySerializer,
    CategoryRetrieveSerializer,
    ProductSerializer,
    ProductRetrieveSerializer,
    ReviewSerializer,
    ReviewRetrieveSerializer,
)



@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    data = CategorySerializer(category, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_retrieve_api_view(request, **kwargs):
    category = Category.objects.get(id=kwargs['id'])
    data = CategoryRetrieveSerializer(category, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_retrieve_api_view(request, **kwargs):
    product = Product.objects.get(id=kwargs['id'])
    data = ProductRetrieveSerializer(product, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_retrieve_api_view(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])
    data = ReviewRetrieveSerializer(review, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)