# book_class.py

class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        :param title: str - The title of the book.
        :param author: str - The author of the book.
        :param year: int - The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message upon object deletion."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the book.
        Returns a human-readable string: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the book.
        Returns a string that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage:
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))  # Calls __str__ method
    print(repr(book1))  # Calls __repr__ method
    del book1  # Calls __del__ method
