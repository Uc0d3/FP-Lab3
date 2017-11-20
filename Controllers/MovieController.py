class MovieController:

    def __init__(self, repository):
        self.repo = repository

    def add_movie(self, movie):
        self.repo.add_movie(movie)

    def find_movie(self, search_term):
        return self.repo.find_movie(search_term)

    def update_price(self, movie, new_price):
        movie.update_price(new_price)

    def print_movies(self):
        for movie in self.repo:
            print(movie)
