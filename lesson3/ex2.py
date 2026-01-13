from book import Book

# Создаем список библиотеки
library = []

# Наполняем список тремя разными экземплярами класса Book
library.append(Book("Преступление и наказание", "Фёдор Достоевский"))
library.append(Book("Мастер и Маргарита", "Михаил Булгаков"))
library.append(Book("1984", "Джордж Оруэлл"))

# Печатаем весь список в нужном формате
for book in library:
    print(f"{book.title} - {book.author}")
    