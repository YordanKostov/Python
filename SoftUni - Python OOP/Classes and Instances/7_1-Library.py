class User:
    books = []

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def get_book(self, author, book_name, days_to_return,library: Library):
        if author in library.books_available.keys() and library.books_available[author] == book_name:
            self.books.append(book_name)
            library.rented_books[author] = book_name
            library.rented_books[author[book_name]] = days_to_return
            del library.books_available[author]
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        elif author in library.rented_books.keys() and library.rented_books[author] == book_name:
            return f"The book {book_name} is already rented and will be available in {library.rented_books[author[book_name]]} days!"

    def return_book(self, author, book_name, library: Library):
        if book_name in self.books:
            self.books.append(book_name)
            library.books_available[author] = book_name
            del library.rented_books[author]
            return
        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ", ".join(self.books)