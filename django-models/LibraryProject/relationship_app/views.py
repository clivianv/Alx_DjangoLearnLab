# relationship_app/views.py

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Book, Library, Author  # Import all necessary models

# --- 1. Function-Based View (FBV) ---


def book_list_view(request):
    """
    Lists all books using a Function-Based View.
    """
    # Use select_related('author') to efficiently retrieve the related Author in one query.
    all_books = Book.objects.select_related('author').all()

    context = {
        'books': all_books,
    }
    # Renders the 'list_books.html' template
    return render(request, 'list_books.html', context)


# --- 2. Class-Based View (CBV) - DetailView ---
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library using a Class-Based View (DetailView).
    """
    model = Library
    # The default template name is <app_name>/<model_name>_detail.html
    # which is 'relationship_app/library_detail.html'
    template_name = 'library_detail.html'
    # The variable name used in the template (e.g., {{ library.name }})
    context_object_name = 'library'

    # Override get_queryset to use prefetch_related for efficiency
    def get_queryset(self):
        # Prefetches the 'books' for the library, and then for each book,
        # selects the 'author' to prevent N+1 queries.
        return Library.objects.prefetch_related('books__author').all()
