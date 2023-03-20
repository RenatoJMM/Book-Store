from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<slug:slug>", views.book_detail_slug, name="book-detail-page"),
    path("thank-you", views.ThankYouView.as_view())
]
