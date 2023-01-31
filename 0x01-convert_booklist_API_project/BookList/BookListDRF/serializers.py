from .models import Book
from rest_framework import serializers


class BookSerializer(serializer.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']