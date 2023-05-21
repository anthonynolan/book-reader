# Create your views here.

from django.shortcuts import render
from .models import Book
import json
import pdb


def index(request):
    books = Book.objects.all()
    print("index")
    return render(request, "loader/list_books.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    stats = {}
    if book.content_file:
        content = book.content_file.read()
        stats["word_count"] = len(content.split())
    book.stats = json.dumps(stats)
    return render(request, "loader/book_detail.html", {"book": book})
