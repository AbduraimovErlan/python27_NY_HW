from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from random import randint
from .models import UserProfile
from .serializers import UserSerializer, ConfirmationSerializer


@api_view(['POST'])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        confirmation_code = generate_confirmation_code()
        user = User.objects.create_user(username=username, password=password, is_active=False)
        user_profile = UserProfile(user=user, confirmation_code=confirmation_code)
        user_profile.save()

        return Response(data={'confirmation_code': confirmation_code}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm_user_view(request):
    serializer = ConfirmationSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        confirmation_code = serializer.validated_data['confirmation_code']

        try:
            user_profile = UserProfile.objects.get(user__username=username, user__is_active=False)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found or already confirmed'}, status=status.HTTP_404_NOT_FOUND)

        if user_profile.confirmation_code == confirmation_code:
            user_profile.user.is_active = True
            user_profile.user.save()
            user_profile.delete()
            return Response({'message': 'User confirmed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def authorization_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'key': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


def generate_confirmation_code():
    return str(randint(100000, 999999))


