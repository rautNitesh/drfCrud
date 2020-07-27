from .models import Book
from rest_framework import serializers, generics
from .models import User

#
# class UserSerializer(serializers.ModelSerializer):
#     books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'books']


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['id', 'name', 'published_year', 'description', 'price', 'owner']




