from django import forms
from .models import Book, Author, Address, Country


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "title": "Title",
            "rating": "Ranting",
            "author": "Author",
            "is_bestselling": "Bestseller",
            "published_countries": "Published Countries"
        }
