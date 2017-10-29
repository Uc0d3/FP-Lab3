class Movie:

    id = 0

    def __init__(self, title, year, rating, price, actors):
        self.title = title
        self.year = year
        self.rating = rating
        self.price = price
        self.actors = actors

    def set_id(self, id):
        self.id = id

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        string = "Id:%d\tName:%s\tYear:%d\tRating:%f\tPrice:%f\nActors:%s"
        return string % (self.id, self.title, self.year, self.rating, self.price, ", ".join(self.actors))
