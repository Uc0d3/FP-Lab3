class MovieController:

    def __init__(self, repository):
        self.repo = repository

    def add_movie(self, movie):
        self.repo.add_movie(movie)

    def print_movies(self):
        for movie in self.repo:
            print(movie)
