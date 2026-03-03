from datetime import date

from author import Author

class Book:
    def __init__(self, isbn: str, title: str, release: date, author: Author) -> None:
        self.isbn: str = isbn
        self.title: str = title
        self.release: date = release
        self.author: Author = author

    @property
    def isbn(self) -> str:
        return self._isbn
    
    @isbn.setter
    def isbn(self, value: str) -> None:
        if not value:
            raise ValueError("isbn can not be empty")
        self._isbn: str = str(value)

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, value: str) -> None:
        if not value:
            raise ValueError("title can not be empty")
        self._title: str = str(value)

    @property
    def release(self) -> date:
        return self._release
    
    @release.setter
    def release(self, value: date) -> None:
        if not isinstance(value, date):
            raise TypeError("release must be a date")
        self._release = value

    @property
    def author(self) -> Author:
        return self._author

    @author.setter
    def author(self, value: Author) -> None:
        if not isinstance(value, Author):
            raise TypeError("author must be an Author instance")
        self._author = value

    # ------------------------------------------------------------------
    # string representations
    # ------------------------------------------------------------------
    def __str__(self) -> str:
        """A human‑readable description of the book."""
        return (
            f"{self.title} ({self.isbn}) – {self.author.firstname} "
            f"{self.author.lastname}, released {self.release}"
        )

    def __repr__(self) -> str:
        return (
            f"Book(isbn={self.isbn!r}, title={self.title!r}, "
            f"release={self.release!r}, author={self.author!r})"
        )
