# api/test_views.py

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints:
      - CRUD operations
      - Filtering, searching, ordering
      - Permissions enforcement (using self.client.login)
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='tester', password='pass1234')

        # Create authors
        self.author1 = Author.objects.create(name='Jane Austen')
        self.author2 = Author.objects.create(name='Mark Twain')

        # Create sample books
        self.book1 = Book.objects.create(
            title='Pride and Prejudice',
            publication_year=1813,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='Adventures of Huckleberry Finn',
            publication_year=1884,
            author=self.author2
        )

    # --- CRUD Operations ---

    def test_list_books_without_authentication(self):
        """GET /api/books/ should list all books (public endpoint)."""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = {item['title'] for item in response.data}
        self.assertSetEqual(titles, {self.book1.title, self.book2.title})

    def test_retrieve_book_detail(self):
        """GET /api/books/<pk>/ should return a book’s details."""
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        self.assertEqual(response.data['publication_year'], self.book1.publication_year)

    def test_create_book_requires_authentication(self):
        """POST /api/books/create/ without auth returns 401."""
        url = reverse('book-create')
        data = {
            'title': 'Emma',
            'publication_year': 1815,
            'author': self.author1.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_with_authentication(self):
        """self.client.login → POST /api/books/create/ should succeed."""
        self.client.login(username='tester', password='pass1234')
        url = reverse('book-create')
        data = {
            'title': 'Emma',
            'publication_year': 1815,
            'author': self.author1.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Emma')
        self.client.logout()

    def test_update_book_requires_authentication(self):
        """PUT /api/books/<pk>/update/ without auth returns 401."""
        url = reverse('book-update', args=[self.book1.pk])
        data = {'title': 'P&P Revised', 'publication_year': 1813}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_with_authentication(self):
        """self.client.login → PUT /api/books/<pk>/update/ should update."""
        self.client.login(username='tester', password='pass1234')
        url = reverse('book-update', args=[self.book1.pk])
        data = {'title': 'P&P Revised', 'publication_year': 1813}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'P&P Revised')
        self.client.logout()

    def test_delete_book_requires_authentication(self):
        """DELETE /api/books/<pk>/delete/ without auth returns 401."""
        url = reverse('book-delete', args=[self.book2.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_with_authentication(self):
        """self.client.login → DELETE /api/books/<pk>/delete/ should delete."""
        self.client.login(username='tester', password='pass1234')
        url = reverse('book-delete', args=[self.book2.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())
        self.client.logout()

    # --- Filtering, Searching, Ordering ---

    def test_filter_books_by_publication_year(self):
        """GET /api/books/?publication_year=1813 returns matching books."""
        url = reverse('book-list') + '?publication_year=1813'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = {item['publication_year'] for item in response.data}
        self.assertSetEqual(years, {1813})

    def test_search_books_by_title(self):
        """GET /api/books/?search=Huck should find Huck Finn."""
        url = reverse('book-list') + '?search=Huck'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [item['title'] for item in response.data]
        self.assertIn('Adventures of Huckleberry Finn', titles)

    def test_order_books_by_publication_year_desc(self):
        """GET /api/books/?ordering=-publication_year lists newest first."""
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [item['publication_year'] for item in response.data]
        self.assertEqual(years, sorted(years, reverse=True))