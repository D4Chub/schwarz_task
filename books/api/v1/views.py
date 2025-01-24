from rest_framework import generics
from books.models import Authors, Genres, Books
from .serializers import (
    AuthorSerializer,
    GenreSerializer,
    BookSerializer,
    BookDetailSerializer
)


class BookListCreateView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return BookSerializer
        return BookDetailSerializer


class AuthorCreateView(generics.CreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class GenreCreateView(generics.CreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class GenreListView(generics.ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
