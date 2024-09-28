from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView,RetrieveUpdateAPIView
from .models import Genre, Author, Book
from .serializers import GenreSerializers


class GenreAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class DeatilGenreView(RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class AuthorAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = GenreSerializers


class DeatilAuthorView(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = GenreSerializers


class BookAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = GenreSerializers


class DeatilBookView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = GenreSerializers
