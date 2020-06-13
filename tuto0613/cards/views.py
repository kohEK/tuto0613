from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from cards.serializers import UserSerializer, CardSerializer
from cards.models import Card


# Create your views here.

class CustomAuthToken(APIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=User.request.data('username'))
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user_id': user.pk, 'token': token.key})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
# *********** permission first//    "detail": "Invalid token."******

# *****************************
