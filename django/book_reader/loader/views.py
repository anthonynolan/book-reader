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


def generate_stats(request, book_id):
    book = Book.objects.get(pk=book_id)
    stats = {}
    if book.description:
        stats["word_count"] = book.description.split()
    import json

    book.stats = json.dumps(stats)
    return render(request, "loader/book_stats.html", {"book": book})
