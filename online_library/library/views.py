from django.shortcuts import render, get_object_or_404
from .models import Author, Book


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})


def book_list(request):
    books = Book.objects.select_related('author')
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    return render(
        request,
        'library/author_detail.html',
        {
            'author': author,
            'books': books,
        }
    )
