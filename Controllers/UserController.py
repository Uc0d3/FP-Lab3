class UserController:

    def __init__(self, repository):
        self.repo = repository

    def add_user(self, user):
        self.repo.add_user(user)

    def print_users(self):
        for user in self.repo:
            print(user)

    def change_lname(self, user, new_name):
        user.update_lname(new_name)
        print("Name changed")

    def find_user(self, search_term):
        return self.repo.find_user(search_term)

    def delete_user(self, user):
        self.repo.delete_user(user)
        print(str(user) + " DELETED")
