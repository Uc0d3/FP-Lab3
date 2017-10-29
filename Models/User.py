class User:

    orders = []
    id = 0

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def update_lname(self, new_name):
        self.l_name = new_name

    def add_order(self, film_id):
        self.orders.append(film_id)

    def set_id(self, id):
        self.id = id
