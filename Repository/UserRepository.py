class UserRepository:

    users = []
    last_id = 0

    def add_user(self, user):
        self.users.append(user)
        self.last_id += 1

    def delete_user(self, user):
        self.users.remove(user)

    def get_by_id(self, id):
        for user in self.users:
            if user["id"] == id:
                return user
