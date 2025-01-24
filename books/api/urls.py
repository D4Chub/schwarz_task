from django.urls import path, include

urlpatterns = [
    path("v1/", include("books.api.v1.urls", namespace="books_v1")),
]