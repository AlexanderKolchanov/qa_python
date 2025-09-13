# Проект для тестирования класса BooksCollector в рамках 4 спринта курса QA Python

## 🎯 Реализованные тесты

### 1. Тестирование получения данных о жанрах
- `test_get_books_genre_empty_collection` - получение пустого словаря из новой коллекции
- `Добавлен отдельный тест для метода get_books_genre` - проверяет возврат словаря с добавленной книгой
- `test_get_books_genre_with_books` - получение словаря жанров после добавления книг

### 2. Тестирование добавления книг
- `test_add_new_book_already_added_book` - попытка добавления уже существующей книги
- `test_add_new_book_name_out_of_range` - добавление книг с некорректной длиной названия
- `test_add_new_book_name_in_the_range` - добавление книг с корректной длиной названия

### 3. Тестирование установки жанров
- `test_set_book_genre_to_existing_book` - установка жанра существующей книге
- `test_set_book_genre_to_not_existing_book` - попытка установки жанра несуществующей книге
- `test_set_book_genre_to_not_existing_genre` - попытка установки несуществующего жанра

### 4. Тестирование получения данных
- `test_get_book_genre_by_name` - получение жанра книги по имени
- `test_get_books_with_specific_genre_multiple_books` - получение нескольких книг по конкретному жанру
- `test_get_books_with_specific_genre_by_wrong_genre` - попытка получения книг по несуществующему жанру
- `test_get_books_for_children` - получение книг, подходящих для детей
- `test_get_books_for_children_adult_rating` - фильтрация книг с возрастным рейтингом

### 5. Тестирование избранного
- `test_add_book_in_favorites` - добавление книги в избранное
- `test_add_book_in_favorites_twice` - повторное добавление книги в избранное
- `test_add_book_in_favorites_not_in_collection` - попытка добавления несуществующей книги в избранное
- `test_delete_book_from_favorites` - удаление книги из избранного
- `test_delete_book_not_in_favorites` - попытка удаления недобавленной книги из избранного
- `test_get_list_of_favorites_books` - получение списка избранных книг

## 📚 Используемые технологии
- **Pytest** - фреймворк для тестирования
- **Фикстуры** - для создания изолированных тестовых окружений
- **Параметризация** - для тестирования различных сценариев

## 🚀 Запуск тестов

```bash
# Все тесты с подробным выводом
pytest -v test.py

# С цветным выводом
pytest -v test.py --color=yes

# Только определенные тесты
pytest -v test.py -k "test_add_new_book"