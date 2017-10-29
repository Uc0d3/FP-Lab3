class UserController:

    def __init__(self, repository):
        self.repo = repository

    def add_user(self, user):
        self.repo.add_user(user)
