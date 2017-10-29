class UserController:

    def __init__(self, repository):
        self.repo = repository

    def add_user(self, user):
        self.repo.add_user(user)

    def print_users(self):
        for user in self.repo:
            print(user)
