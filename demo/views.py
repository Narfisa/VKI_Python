from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.

def first(request):
    return render(request, 'test.html', {'data': 'Hello! I am some data from `first` func!'})

class Second(View):
    books = Book.objects.all()
    output = f'We have {len(books)} books in our DB (Yohoooo!)'

    def get(self,request):
        return HttpResponse(self.output)