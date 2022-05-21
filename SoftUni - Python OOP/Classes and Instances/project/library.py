class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def __init__(self):
        pass

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
            return
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
            if user in self.rented_books:
                del self.rented_books[user]
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        filtered_usernames = [un for un in self.user_records if un.user_id == user_id]
        if filtered_usernames:
            user = filtered_usernames[0]
            if not user.username == new_username:
                old_username = user.username
                user.username = new_username
                if old_username in self.rented_books:
                    books_for_user = self.rented_books[old_username]
                    del self.rented_books[old_username]
                    self.rented_books[user.username] = books_for_user
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            else:
                return "Please check again the provided username - it should be different than the username used so " \
                       "far! "
        else:
            return f"There is no user with id = {user_id}!"
