# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, "loader/list_books.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "loader/book_detail.html", {"book": book})
