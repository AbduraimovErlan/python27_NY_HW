from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from random import randint

users = {}

@api_view(['POST'])
def registration_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username in users:
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

    confirmation_code = generate_confirmation_code()  # Генерация случайного 6-значного кода
    users[username] = {'password': password, 'confirmed': False, 'confirmation_code': confirmation_code}

    return Response(data={'confirmation_code': confirmation_code}, status=status.HTTP_200_OK)


@api_view(['POST'])
def confirm_user_view(request):
    username = request.data.get('username')
    confirmation_code = request.data.get('confirmation_code')

    if username not in users:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user = users[username]
    if user['confirmed']:
        return Response({'error': 'User already confirmed'}, status=status.HTTP_400_BAD_REQUEST)

    if user['confirmation_code'] == confirmation_code:
        user['confirmed'] = True
        return Response({'message': 'User confirmed successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def authorization_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username not in users:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user = users[username]
    if not user['confirmed']:
        return Response({'error': 'User not confirmed'}, status=status.HTTP_401_UNAUTHORIZED)

    if user['password'] == password:
        return Response({'message': 'User authorized successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)


def generate_confirmation_code():
    return str(randint(100000, 999999))

