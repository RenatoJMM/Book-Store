from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404, HttpResponseRedirect
from django.db.models import Avg, Max, Min

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .forms import BookForm

# Create your views here.


class IndexView(View):
    def get(self, request):

        books = Book.objects.all().order_by("-title")
        num_books = books.count()
        statistics = books.aggregate(Avg("rating"), Min("rating"))

        form = BookForm()

        return render(request, "book_outlet/index.html", {
            "form": form,
            "books": books,
            "num_books": num_books,
            "statistics": statistics
        })

    def post(self, request):
        form = BookForm(request.POST)
        books = Book.objects.all().order_by("-title")
        num_books = books.count()
        statistics = books.aggregate(Avg("rating"), Min("rating"))

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "book_outlet/index.html", {
            "form": form,
            "books": books,
            "num_books": num_books,
            "statistics": statistics
        })


# def index(request):
#     books = Book.objects.all().order_by("-title")
#     num_books = books.count()
#     average_rating = books.aggregate(
#         Avg("rating"), Min("rating"))  # rating__avg, rating__min

#     return render(request, "book_outlet/index.html", {
#         "books": books,
#         "num_books": num_books,
#         "average_rating": average_rating
#     })

    """     try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404() 
    """


class AllBooksView(ListView):
    template_name = "book_outlet/all_books.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        context['books'] = books
        context['num_books'] = books.count()
        context['statistics'] = books.aggregate(Avg("rating"), Min("rating"))

        return context


def book_detail_slug(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling,
        "slug": book.slug
    })


class ThankYouView(TemplateView):
    template_name = "book_outlet/thank-you.html"
