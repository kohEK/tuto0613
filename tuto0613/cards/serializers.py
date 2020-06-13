from rest_framework import serializers
from django.contrib.auth.models import User
from cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['owner', 'card_color', 'register_date']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserSerializer(serializers.ModelSerializer):
    card = CardSerializer(source='card_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'card', 'email']
# fields
