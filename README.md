# QA Python 4 Sprint - BooksCollector Project

Проект для тестирования класса BooksCollector в рамках 4 спринта курса QA Python

## Реализованные тесты

### 1. Тестирование добавления книг
- `test_add_new_book_add_two_books` - добавление двух разных книг
- `test_add_new_book_already_added_book` - попытка добавления уже существующей книги
- `test_add_new_book_name_out_of_range` - добавление книг с некорректной длиной названия
- `test_add_new_book_name_in_the_range` - добавление книг с корректной длиной названия

### 2. Тестирование установки жанров
- `test_set_book_genre_to_existing_book` - установка жанра существующей книге
- `test_set_book_genre_to_not_existing_book` - попытка установки жанра несуществующей книге
- `test_set_book_genre_to_not_existing_genre` - попытка установки несуществующего жанра

### 3. Тестирование получения данных
- `test_get_book_genre_by_name` - получение жанра книги по имени
- `test_get_books_with_specific_genre_by_genre` - получение книг по конкретному жанру
- `test_get_books_with_specific_genre_by_wrong_genre` - попытка получения книг по несуществующему жанру
- `test_get_books_for_children` - получение книг, подходящих для детей
-  `test_get_books_for_children_adult_rating` - попытка получения книг с возрастным рейтингом
    

### 4. Тестирование избранного
- `test_add_book_in_favorites_not_added_in_favorites_book` - добавление книги в избранное
- `test_add_book_in_favorites_added_in_favorites_book` - повторное добавление книги в избранное
- `test_add_book_in_favorites_not_added_dict_book` - попытка добавления несуществующей книги в избранное
- `test_delete_book_from_favorites` - удаление книги из избранного
- `test_delete_book_from_favorites_deleted_book` - попытка удаления недобавленной книги из избранного
- `test_get_list_of_favorites_books` - получение списка избранных книг

## Используемые книги
- 1984
- Маленький принц
- The Girl with Seven Names
- The Fight Club
- Скотный двор

## Запуск тестов

```bash
pytest -v test.py