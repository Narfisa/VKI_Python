from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.

def first(request):
    books = Book.objects.all()
    return render(request, 'test.html', {'data': books})

class Second(View):
    books = Book.objects.all()
    output = f'We have {len(books)} books in our DB (Yohoooo!)'

    def get(self,request):
        return HttpResponse(self.output)