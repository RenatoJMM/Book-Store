from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail_slug, name="book-detail-page")
]