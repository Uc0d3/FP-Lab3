class UserController:

    def __init__(self, repository):
        self.repo = repository

    def add_user(self, user):
        self.repo.add_user(user)

    def print_users(self):
        for user in self.repo:
            print(user)

    def change_lname(self):
        search_term = input("Search Term:")
        user = self.repo.find_user(search_term)
        if user is not None:
            new_name = input("New First Name:")
            user.update_lname(new_name)
            print("Name changed")

    def delete_user(self):
        search_term = input("Search Term:")
        user = self.repo.find_user(search_term)
        if user is not None:
            self.repo.delete_user(user)
            print(str(user) + " DELETED")
