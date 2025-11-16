from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# -----------------------------------------
# FUNCTION-BASED VIEW (FBV)
# -----------------------------------------

def list_books(request):
    """
    Displays all books and their authors.
    """
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# -----------------------------------------
# CLASS-BASED VIEW (CBV)
# -----------------------------------------

class LibraryDetailView(DetailView):
    """
    Displays details of a specific library and its books.
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
