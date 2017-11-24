class User:

    id = 0
    orders = []

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def update_lname(self, new_name):
        self.l_name = new_name

    def add_order(self, film_id):
        self.orders.append(film_id)

    def set_id(self, id):
        self.id = id

    def __str__(self):
        string = "Id:%d\tFirst Name:%s\tLast Name:%s\tOrders:%s"
        orders = list(map(str, self.orders))
        return string % (self.id, self.f_name, self.l_name, ", ".join(orders))
