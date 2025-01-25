class Book:
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a human-readable string for the Book instance."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        :param title: The title of the book.
        :param author: The author of the book.
        :param file_size: The file size of the EBook in MB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a human-readable string for the EBook instance."""
        return f"EBook: {self.title} by {self.author},File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        :param title: The title of the book.
        :param author: The author of the book.
        :param page_count: The number of pages in the print book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a human-readable string for the PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
