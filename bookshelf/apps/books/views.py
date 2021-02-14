from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


def index(request):
    best_book_list = Book.objects.order_by('-created_at')[:5]
    context = {'best_book_list': best_book_list}
    return render(request, 'books/index.html', context)


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        data = serializer.data
        book.delete()
        return Response(data)
