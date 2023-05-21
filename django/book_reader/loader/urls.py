from django.urls import path

from . import views

app_name = "loader"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:book_id>/", views.book_detail, name="book_detail"),
]
