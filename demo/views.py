from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from .serializers import BookSerializer

# Create your views here.

from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()


class First(View):
    books = Book.objects.all()

    def get(self, request):
        return render(request, 'test.html', {'books': self.books})

class Second(View):
    books = Book.objects.all()
    output = f'We have {len(books)} books in our DB (Yohoooo!)'

    def get(self,request):
        return HttpResponse(self.output)