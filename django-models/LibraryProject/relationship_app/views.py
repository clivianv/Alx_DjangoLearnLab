# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import all necessary models

# --- 1. Function-Based View (FBV) ---


def book_list_view(request):
    """
    Lists all books using a Function-Based View.
    """
    # **This is where Book.objects.all() or similar is used.**
    # Use select_related('author') for performance.
    all_books = Book.objects.select_related('author').all()

    context = {
        'books': all_books,
    }
    # **This is where 'list_books.html' is referenced.**
    return render(request, 'list_books.html', context)


# --- 2. Class-Based View (CBV) - DetailView ---
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library using a Class-Based View (DetailView).
    """
    model = Library
    # The template name specified here is 'library_detail.html'
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        # Prefetches the 'books' for the library, and then for each book,
        # selects the 'author' to prevent N+1 queries.
        return Library.objects.prefetch_related('books__author').all()
