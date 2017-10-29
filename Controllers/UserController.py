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
        user = self.find_user(search_term)
        if user is not None:
            new_name = input("New First Name:")
            user.update_lname(new_name)
            print("Name changed")

    def delete_user(self):
        search_term = input("Search Term:")
        user = self.find_user(search_term)
        if user is not None:
            self.repo.delete_user(user)
            print(str(user) + " DELETED")

    def find_user(self, term, key=None):
        found = []
        for user in self.repo:
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
        print("Multiple user Found:")
        for f_user in found:
            print(f_user)
        id = int(input("Please choose an id from the list above:"))
        return(self.repo.get_by_id(id))
