from django.shortcuts import render

from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


def index(request):
    best_book_list = Book.objects.order_by('-created_at')[:5]
    context = {'best_book_list': best_book_list}
    return render(request, 'books/index.html', context)


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
