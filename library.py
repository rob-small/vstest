class Library:
    """A class representing a library of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = {}

    def add_book(self, title, author):
        """Add a book to the library's collection.

        Parameters:
        title (str): The title of the book to add.
        author (str): The author of the book to add.
        """
        if title not in self.books:
            self.books[title] = {
                "author": author,
                "available": True
            }

    def check_out(self, title: str) -> bool:
        """
        Checks out a book from the library's collection.

        Parameters:
        title (str): The title of the book to check out.

        Returns:
        bool: True if the book was successfully checked out, False otherwise.
        """
        if title in self.books and self.books[title]["available"]:
            self.books[title]["available"] = False
            return True
        return False

    def check_in(self, title: str) -> bool:
        """
        Checks a book back into the library's collection.

        Parameters:
        title (str): The title of the book to check in.

        Returns:
        bool: True if the book was successfully checked in, False otherwise.
        """
        if title in self.books:
            self.books[title]["available"] = True
            return True
        return False

    def is_available(self, title: str) -> bool:
        """
        Checks if a book is available in the library's collection.

        Parameters:
        title (str): The title of the book to check.

        Returns:
        bool: True if the book is available, False otherwise.
        """
        if title in self.books:
            return self.books[title]["available"]
        return False

    def list_books(self) -> str:
        """
        Lists all books in the library collection, including their titles and authors.

        Parameters:
        None

        Returns:
        str: A string of book titles and authors.
        """
        book_list = [f"{title} by {self.books[title]['author']}" for title in self.books]
        return "\n".join(book_list)  

import unittest

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("The Catcher in the Rye", "J. D. Salinger")
        self.assertIn("The Catcher in the Rye", self.library.books)
        self.assertEqual(self.library.books["The Catcher in the Rye"]["author"], "J. D. Salinger")

    def test_check_out(self):
        self.library.add_book("The Catcher in the Rye", "J. D. Salinger")
        self.library.check_out("The Catcher in the Rye")
        self.assertFalse(self.library.is_available("The Catcher in the Rye"))

    def test_check_in(self):
        self.library.add_book("The Catcher in the Rye", "J. D. Salinger")
        self.library.check_out("The Catcher in the Rye")
        self.library.check_in("The Catcher in the Rye")
        self.assertTrue(self.library.is_available("The Catcher in the Rye"))

    def test_list_books(self):
        self.library.add_book("The Catcher in the Rye", "J. D. Salinger")
        self.library.add_book("To Kill a Mockingbird", "Harper Lee")
        self.assertEqual(self.library.list_books(), "The Catcher in the Rye by J. D. Salinger\nTo Kill a Mockingbird by Harper Lee")

if __name__ == '__main__':
    unittest.main()
