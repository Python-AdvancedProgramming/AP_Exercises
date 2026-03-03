from typing import List

from book import Book


class Library:
    def __init__(self, books: List[Book] | None = None) -> None:
        # use the property setter so validation runs
        self.books = books or []

    @property
    def books(self) -> List[Book]:
        """A list of books contained in the library."""
        return self._books

    @books.setter
    def books(self, value: List[Book]) -> None:
        if value is None:
            self._books = []
            return
        if not isinstance(value, list):
            raise TypeError("books must be a list of Book instances")
        for item in value:
            if not isinstance(item, Book):
                raise TypeError("all items in books must be Book instances")
        self._books = value

    def add_book(self, book: Book) -> None:
        """Append a book to the collection."""
        if not isinstance(book, Book):
            raise TypeError("book must be a Book")
        self._books.append(book)

    def remove_book(self, book: Book) -> None:
        """Remove a book from the collection; ValueError if not present."""
        self._books.remove(book)

    def find_by_title(self, title: str) -> List[Book]:
        """Return all books whose title contains the given string."""
        return [b for b in self._books if title.lower() in b.title.lower()]

    def __len__(self) -> int:
        return len(self._books)

    # --------------------------------------------------------------
    # string representations
    # --------------------------------------------------------------
    def __str__(self) -> str:
        """A human-readable summary showing how many books are present."""
        return f"Library with {len(self)} book(s)"

    def __repr__(self) -> str:
        return f"Library(books={len(self)})"
