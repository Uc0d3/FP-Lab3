from Models.User import User
from Models.Movie import Movie


class UI:

    menu = """
1 - Add User
2 - Add Movie
3 - Show Users
4 - Show Movies
5 - Update Last Name
6 - Delete User
7 - Update Movie Price
8 - Order Movies
9 - Show Users with orders
10 - Filter Movie by Rating
11 - Show Movies with the given actor
Option:
    """.strip()

    def __init__(self, user_controller, movie_controller):
        self.user_c = user_controller
        self.movie_c = movie_controller

    def read_menu(self):
        return int(input(self.menu))

    def read_user(self):
        f_name = input("First Name:")
        l_name = input("Last Name:")
        user = User(f_name, l_name)
        return user

    def change_lname(self):
        search_term = input("Search Term:")
        user = self.user_c.find_user(search_term)
        if user is not None:
            new_name = input("New First Name:")
            user = self.user_c.change_lname(user, new_name)

    def delete_user(self):
        search_term = input("Search Term:")
        user = self.user_c.find_user(search_term)
        if user is not None:
            self.user_c.delete_user(user)

    def change_movie_price(self):
        search_term = input("Search Term:")
        movie = self.movie_c.find_movie(search_term)
        if movie is not None:
            new_price = float(input("New Price"))
            self.movie_c.update_price(movie, new_price)
            print("Price for %d changed to %f" % (movie.id, new_price))

    def show_users_with_orders(self):
        users = self.user_c.get_users_with_orders()
        for user in users:
            print(str(user))

    def filter_movies_by_rating(self):
        rating = float(input("Rating:"))
        filtered_movies = self.movie_c.filter_by_rating(rating)
        for movie in filtered_movies:
            print(str(movie))

    def show_movies_with_actor(self):
        actor = input("Actor:")
        movies = self.movie_c.get_movies_with_actor(actor)
        if movies:
            for movie in movies:
                print(movie)
        else:
            print("No Movies with %s found" % actor)

    def make_order(self):
        search_term = input("User Search Term:")
        user = self.user_c.find_user(search_term)
        if user is not None:
            print("Finish order by typing done")
            orders = []
            search_term = input("Movie Search Term:")
            while("done" not in search_term.lower()):
                movie = self.movie_c.find_movie(search_term)
                if movie is not None:
                    orders.append(movie)
                    print(str(movie) + " added to cart")
                search_term = input("Movie Search Term:")
            order_price = sum(order.price for order in orders)
            print("Order price:" + str(order_price))
            print("Y - Confirm\nN - Cancel\nInput:")
            if input() == "Y":
                self.user_c.add_orders(user, orders)
                print("Order added to user " + user.f_name)
            else:
                print("Order cancaled")

    def read_movie(self):
        title = input("Title:")
        year = int(input("Year:"))
        rating = float(input("Rating:"))
        price = float(input("Price:"))
        actors = input("Actors (comma separated):")
        actors = actors.strip()
        actors = actors.split(",")
        actors = list(map(str.strip, actors))
        movie = Movie(title, year, rating, price, actors)
        return movie

    def start(self):
        while True:
            op = self.read_menu()
            if op == 1:
                user = self.read_user()
                self.user_c.add_user(user)
            if op == 2:
                movie = self.read_movie()
                self.movie_c.add_movie(movie)
            if op == 3:
                self.user_c.print_users()
            if op == 4:
                self.movie_c.print_movies()
            if op == 5:
                self.change_lname()
            if op == 6:
                self.delete_user()
            if op == 7:
                self.change_movie_price()
            if op == 8:
                self.make_order()
            if op == 9:
                self.show_users_with_orders()
            if op == 10:
                self.filter_movies_by_rating()
            if op == 11:
                self.show_movies_with_actor()
