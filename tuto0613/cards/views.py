from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from cards.serializers import UserSerializer, CardSerializer, UserCreateSerializer
from cards.models import Card
from cards.permissions import IsOwnerOrReadOnly



class MyPagination(CursorPagination):
    page_size = 3
    ordering = '-id'

# Create your views here.

class CustomAuthToken(APIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user_id': user.pk, 'token': token.key})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    # serializer_class = UserSerializer
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action in ['update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        else:
            return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            serializer_class = UserCreateSerializer
            return serializer_class
        else:
            serializer_class = UserSerializer
            return serializer_class


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
