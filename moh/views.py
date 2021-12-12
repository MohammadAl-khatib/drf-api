from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book
from .serilaizers import BookSerializer
from rest_framework import generics

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer