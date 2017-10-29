from Models.User import User


class UserRepository:

    users = []
    last_id = 0

    def add_user(self, user):
        user.set_id(self.last_id + 1)
        self.users.append(user)
        self.last_id += 1

    def delete_user(self, user):
        self.users.remove(user)

    def get_by_id(self, id):
        for user in self.users:
            if user.id == id:
                return user
        print("Invalid ID")

    def load_from_file(self, file_name):
        f = open(file_name)
        for line in f:
            try:
                data = line.split(",")
                f_name = data[0].strip()
                l_name = data[1].strip()
                orders = data[2].strip().split(":")
                new_user = User(f_name, l_name)
                new_user.orders = orders
                self.add_user(new_user)
            except IndexError as e:
                print("Corrupted user read, skipped")
        print("Users loaded from file")

    def __iter__(self):
        for user in self.users:
            yield user