from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    AuthorCreateView,
    GenreCreateView,
)

app_name = 'books'

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book_retrieve_update_destroy'),
    path('authors/', AuthorCreateView.as_view(), name='create_author'),
    path('genres/', GenreCreateView.as_view(), name='create_genre'),
]
