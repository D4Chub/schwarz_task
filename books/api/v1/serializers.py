from rest_framework import serializers
from books.models import Authors, Genres, Books

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = [
            'id',
            'name',
            'last_name',
            'middle_name',
        ]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = [
            'id',
            'name',
        ]

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Authors.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genres.objects.all())

    class Meta:
        model = Books
        fields = [
            'id',
            'name',
            'author',
            'genre',
            'publishing_year'
        ]


class BookDetailSerializer(BookSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer()

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ['author', 'genre']
