from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    AuthorListView,
    GenreListView,
    AuthorCreateView,
    GenreCreateView,
)

app_name = 'books'

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book_retrieve_update_destroy'),
    path('authors/create/', AuthorCreateView.as_view(), name='create_author'),
    path('genres/create/', GenreCreateView.as_view(), name='create_genre'),
    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
]
