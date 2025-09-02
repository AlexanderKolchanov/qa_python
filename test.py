import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Маленький принц')
        assert collector.get_books_genre() == {'1984': '',
                                               'Маленький принц': ''}
        
        
    def test_add_new_book_already_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert collector.get_books_genre() == {'1984': ''}


    @pytest.mark.parametrize('name', ['',
                                      'Очень длинное название книги которое точно превышает лимит в сорок символов',
                                      'Невероятно длинное название книги которое не должно быть добавлено в коллекцию'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0      


    @pytest.mark.parametrize('name', ['1984',
                                      'Маленький принц',
                                      'The Girl',
                                      'Я'])
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()


    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_books_genre() == {'1984': 'Фантастика'}


    def test_set_book_genre_to_not_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_books_genre() == {}


    def test_set_book_genre_to_not_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Драма')
        assert collector.get_books_genre() == {'1984': ''}


    @pytest.mark.parametrize('name, genre', [('The Fight Club', 'Ужасы'),
                                             ('Скотный двор', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre


    @pytest.mark.parametrize('name, genre', [('The Fight Club', 'Ужасы'),
                                             ('Скотный двор', 'Комедии')])
    def test_get_books_with_specific_genre_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name] 


    def test_get_books_with_specific_genre_by_wrong_genre(self, my_books_collection):
        assert len(my_books_collection.get_books_with_specific_genre('Драма')) == 0


    def test_get_books_for_children(self, my_books_collection):
        assert len(my_books_collection.get_books_for_children()) == 3
        assert my_books_collection.get_books_for_children() == ['1984', 'Маленький принц', 'Скотный двор']


    def test_get_books_for_children_adult_rating(self, books_collection):
    # Добавляем книги с возрастным рейтингом
        books_collection.add_new_book('The Fight Club')
        books_collection.add_new_book('The Girl with Seven Names')
        books_collection.set_book_genre('The Fight Club', 'Ужасы')  # Жанр с возрастным рейтингом
        books_collection.set_book_genre('The Girl with Seven Names', 'Детективы')  # Жанр с возрастным рейтингом
    
    # Добавляем детскую книгу для контроля
        books_collection.add_new_book('Маленький принц')
        books_collection.set_book_genre('Маленький принц', 'Мультфильмы')  # Жанр без возрастного рейтинга
    
    # Проверяем, что только детская книга в списке
        children_books = books_collection.get_books_for_children()
        assert len(children_books) == 1
        assert children_books == ['Маленький принц']
        assert 'The Fight Club' not in children_books
        assert 'The Girl with Seven Names' not in children_books    


    def test_add_book_in_favorites_not_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('1984')
        assert '1984' in my_books_collection.get_list_of_favorites_books()
        assert len(my_books_collection.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('1984')
        my_books_collection.add_book_in_favorites('1984')
        assert '1984' in my_books_collection.get_list_of_favorites_books()
        assert len(my_books_collection.get_list_of_favorites_books()) == 1


    def test_add_book_in_favorites_not_added_dict_book(self, my_books_collection):
        book = 'Неизвестная книга'
        my_books_collection.add_book_in_favorites(book)
        assert len(my_books_collection.get_list_of_favorites_books()) == 0


    def test_delete_book_from_favorites(self, my_books_collection):
        my_books_collection.add_book_in_favorites('1984')
        my_books_collection.delete_book_from_favorites('1984')
        assert len(my_books_collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_deleted_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('1984')
        my_books_collection.delete_book_from_favorites('Маленький принц')
        assert len(my_books_collection.get_list_of_favorites_books()) == 1
        assert 'Маленький принц' not in my_books_collection.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, my_books_collection):
        my_books_collection.add_book_in_favorites('1984')
        my_books_collection.add_book_in_favorites('Маленький принц')
        assert my_books_collection.get_list_of_favorites_books() == ['1984', 'Маленький принц']            


