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
                orders = data[2].strip()
                new_user = User(f_name, l_name)
                if orders:
                    orders = orders.split(":")
                    orders = list(map(int, orders))
                    print(orders)
                    new_user.orders = orders
                self.add_user(new_user)
            except IndexError as e:
                print("Corrupted user read, skipped " + str(e))
        print("Users loaded from file")

    def find_user(self, term, key=None):
        found = []
        for user in self.users:
            if key is not None:
                if term.lower() in str(getattr(user, key)).lower():
                    found.append(user)
            else:
                members = [attr for attr in dir(user) if not callable(getattr(user, attr)) and not attr.startswith("__")]
                for member in members:
                    user_prop = str(getattr(user, member)).lower()
                    if term.lower() in user_prop:
                        found.append(user)
                        break
        if len(found) == 0:
            print("No User Found")
            return None
        if len(found) == 1:
            user = found[0]
            print("Found User:" + str(user))
            return user
        print("Multiple Users Found:")
        for f_user in found:
            print(f_user)
        id = int(input("Please choose an id from the list above:"))
        return(self.get_by_id(id))

    def __iter__(self):
        for user in self.users:
            yield user
