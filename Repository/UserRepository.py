from Models.User import User


class UserRepository:

    users = []
    last_id = 0
    file_name = "users.csv"

    def __init__(self, file_name):
        self.file_name = file_name

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

    def load_from_file(self):
        f = open(self.file_name)
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
                    new_user.orders = orders
                self.add_user(new_user)
            except IndexError as e:
                print("Corrupted user read, skipped " + str(e))
        print("Users loaded from file")
        f.close()

    def find_user(self, term, key=None, silent=False):
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
            if not silent:
                print("No User Found")
            return None
        if len(found) == 1:
            user = found[0]
            if not silent:
                print("Found User:" + str(user))
            return user
        if not silent:
            print("Multiple Users Found:")
        for f_user in found:
            if not silent:
                print(f_user)
        if not silent:
            id = int(input("Please choose an id from the list above:"))
        return(self.get_by_id(id))

    def save_to_file(self):
        f = open(self.file_name, "w")
        for user in self.users:
            csv = "%s,%s,%s\n"
            orders = list(map(str, user.orders))
            csv = csv % (user.f_name, user.l_name, ":".join(orders))
            f.write(csv)
        f.close()

    def __iter__(self):
        for user in self.users:
            yield user
