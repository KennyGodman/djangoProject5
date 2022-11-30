from django.urls import path

from . import views

# app_name = "book"

urlpatterns = [
    # path("index/", views.index, name="book-list"),
    path("indexTwo/", views.index_two, name="book-list")
]
