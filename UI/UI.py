from Models.User import User
from Models.Movie import Movie


class UI:

    menu = """
1 - Add User
2 - Add Movie
3 - Show Users
4 - Show Movies
5 - Update First Name
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

    def read_movie(self):
        title = input("Title:")
        year = int(input("Year:"))
        rating = float(input("Rating:"))
        price = float(input("Price:"))
        actors = input("Actors (comma separated):")
        actors = actors.strip()
        actors = actors.split(",")
        actors = map(str.strip, actors)
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
                self.user_c.change_lname()
