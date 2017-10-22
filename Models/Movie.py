class Movie:

    def __init__(self, id, title, year, rating, price, actors):
        self.id = id
        self.title = title
        self.year = year
        self.rating = rating
        self.price = price
        self.actors = actors

    def update_price(self, new_price):
        self.price = new_price
