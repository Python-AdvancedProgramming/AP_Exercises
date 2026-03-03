from datetime import date

from author import Author
from book import Book
from library import Library


def main() -> None:
    # authors (famous computer scientists)
    ada = Author("Ada", "Lovelace")
    alan = Author("Alan", "Turing")
    donald = Author("Donald", "Knuth")
    edsger = Author("Edsger", "Dijkstra")
    grace = Author("Grace", "Hopper")

    # books (associated with the authors)
    ada_book = Book("N/A", "Notes on the Analytical Engine", date(1843, 7, 1), ada)
    alan_book = Book("N/A", "On Computable Numbers", date(1936, 11, 1), alan)
    knuth_book = Book("9780201896831", "The Art of Computer Programming", date(1968, 1, 1), donald)
    dijkstra_book = Book("N/A", "A Discipline of Programming", date(1976, 1, 1), edsger)
    hopper_book = Book("N/A", "The Education of a Computer", date(1952, 1, 1), grace)

    # build a library
    lib = Library([ada_book, alan_book, knuth_book, dijkstra_book, hopper_book])

    print(f"Library contains {len(lib)} books:")
    for book in lib.books:
        print("  ", book)


if __name__ == "__main__":
    main()
