from rest_framework.test import APITestCase
from rest_framework import status, reverse
from books.models import Authors, Genres, Books

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.author = Authors.objects.create(name="John", last_name="Doe")
        self.genre = Genres.objects.create(name="Fiction")

        self.book = Books.objects.create(
            name="Test Book",
            author=self.author,
            genre=self.genre,
            publishing_year="2025-10-10"
        )
        
        self.book_data = {
            "name": "New Book Title",
            "author": self.author.id,
            "genre": self.genre.id,
            "publishing_year": "2025-10-10"
        }

        self.book_update_data = {
            "name": "Updated Book Title",
            "author": self.author.id,
            "genre": self.genre.id,
            "publishing_year": "2026-10-10"
        }

    def test_create_book(self):
        response = self.client.post(f"/api/v1/books/", self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.book_data['name'])


    def test_get_book_detail(self):
        response = self.client.get(f"/api/v1/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.book.name)
        self.assertEqual(response.data['author']['id'], self.author.id)
        self.assertEqual(response.data['genre']['id'], self.genre.id)

    def test_update_book(self):
        response = self.client.put(f"/api/v1/books/{self.book.id}/", self.book_update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.book_update_data['name'])
        self.assertEqual(response.data['publishing_year'], self.book_update_data['publishing_year'])

    def test_delete_book(self):
        response = self.client.delete(f"/api/v1/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/api/v1/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_author(self):
        author_data = {
            "name": "New Author",
            "last_name": "Smith",
            "middle_name": "Middle"
        }
        response = self.client.post("/api/v1/authors/", author_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], author_data['name'])

    def test_create_genre(self):
        genre_data = {
            "name": "Science Fiction"
        }
        response = self.client.post("/api/v1/genres/", genre_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], genre_data['name'])

    def test_list_authors(self):
        response = self.client.get("/api/v1/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_genres(self):
        response = self.client.get("/api/v1/genres/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
