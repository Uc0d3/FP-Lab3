class UserController:

    def __init__(self, repository):
        self.repo = repository

    def add_user(self, user):
        self.repo.add_user(user)
        self.repo.save_to_file()

    def print_users(self):
        for user in self.repo:
            print(user)

    def change_lname(self, user, new_name):
        user.update_lname(new_name)
        self.repo.save_to_file()
        print("Name changed")

    def add_orders(self, user, orders):
        for order in orders:
            user.add_order(order.id)
        self.repo.save_to_file()

    def find_user(self, search_term, key=None, silent=False):
        return self.repo.find_user(search_term, key, silent)

    def get_users_with_orders(self):
        found_users = [user for user in self.repo if user.orders]
        return found_users

    def delete_user(self, user):
        self.repo.delete_user(user)
        self.repo.save_to_file()
        print(str(user) + " DELETED")
