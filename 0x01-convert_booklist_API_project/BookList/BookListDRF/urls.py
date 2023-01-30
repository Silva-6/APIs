from django.urls import path
from .models import BookView


urlpatterns = [
    path('books', BookView.as_viev()),
]