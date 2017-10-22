class User:

    orders = []

    def __init__(self, id, f_name, l_name):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name

    def update_lname(self, new_name):
        self.l_name = new_name

    def add_order(self, film_id):
        self.orders.append(film_id)
