# OOP Exercise: Library Classes

In this exercise you will design and implement a small object‑oriented model of a library.  The `solutions/library` package in the repository contains a working reference implementation; your task is to build your own version from scratch following the requirements below.

> **Note**: Do not copy the solution files directly—this exercise is meant to be solved independently. Once you have finished your implementation, compare it with the provided `solutions/library` package to see alternate design choices.

## Learning goals

1. Practice defining classes with attributes, properties, and validation logic.
2. Use composition to model relationships between objects.
3. Implement special methods such as `__str__`, `__repr__`, and `__len__`.
4. Write clear docstrings and follow good naming conventions.

---

## Requirements

You should create the following classes in a new package or module (e.g. `library.py`, `book.py`, `author.py`):

### `Author`
- Attributes:
  - `firstname` (string) – cannot be empty.
  - `lastname` (string) – cannot be empty.
- Use properties with setters to validate the values.
- No other behaviour is required.

### `Book`
- Attributes:
  - `isbn` (string) – must not be empty.
  - `title` (string) – must not be empty.
  - `release` (`datetime.date`) – must be a `date` instance.
  - `author` (an `Author` instance) – use composition.
- Properties should enforce the type/validation rules listed above.
- Implement `__str__` to return a human‑readable description of the book, including title, isbn, author name, and release date.
- Implement `__repr__` to return an unambiguous representation like `<Book 'isbn' 'title'>`.

### `Library`
- Manage a collection of `Book` objects.
- The constructor may receive an initial list of books (default to empty).
- Implement a `books` property that ensures the value is always a list of `Book` instances and never `None`.
- Methods:
  - `add_book(book)` – add a `Book` to the collection, raising `TypeError` for invalid arguments.
  - `remove_book(book)` – remove a book, propagating the `ValueError` if the book is not present.
  - `find_by_title(title)` – return a list of all books whose titles contain the given string (case‑insensitive).
- Implement `__len__` so that `len(library)` returns the number of books.

---

## Optional extensions

- Add a method `find_by_author(author_name)` that searches by the author's first or last name.
- Support equality comparison for `Book` objects based on ISBN.

---

Good luck and have fun building your library!
