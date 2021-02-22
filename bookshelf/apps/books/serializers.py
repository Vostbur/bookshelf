from rest_framework import serializers
from .models import Book

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class BookSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'created_at', 'users')
        depth = 1
