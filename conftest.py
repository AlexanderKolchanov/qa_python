import pytest
from main import BooksCollector


@pytest.fixture
def books_collection():
    books_collection = BooksCollector()
    return books_collection


@pytest.fixture
def my_books_collection(books_collection):
    my_collection = books_collection
    books = ['1984', 'The Fight Club', 'The Girl with Seven Names', 'Маленький принц', 'Скотный двор']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    
    for i in range(5):
        my_collection.add_new_book(books[i])
    
    for i in range(5):
        my_collection.set_book_genre(books[i], genre[i])
    
    return my_collection