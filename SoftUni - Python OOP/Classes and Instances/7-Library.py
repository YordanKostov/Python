class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def __init__(self):
        pass

    def add_user(self, user: User):
        if user not in self.user_records:
            self.user_records.append(user)
            return
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User):
        if user in self.user_records:
            self.user_records.remove(user)
            return
        return f"We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        filtered_usernames = [un for un in self.user_records if un.user_id == user_id]
        #if filtered_usernames[0].username != new_username:


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


user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)