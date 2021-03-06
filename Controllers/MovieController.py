class MovieController:

    def __init__(self, repository):
        self.repo = repository

    def add_movie(self, movie):
        self.repo.add_movie(movie)
        self.repo.save_to_file()

    def find_movie(self, search_term, key=None, silent=False):
        return self.repo.find_movie(search_term, key, silent)

    def update_price(self, movie, new_price):
        movie.update_price(new_price)
        self.repo.save_to_file()
        

    def filter_by_rating(self, rating):
        found_movies = [movie for movie in self.repo if movie.rating > rating]
        return found_movies

    def get_movies_with_actor(self, actor):
        found_movies = []
        for movie in self.repo:
            if actor.lower() in list(map(str.lower, movie.actors)):
                found_movies.append(movie)
        return found_movies

    def print_movies(self):
        for movie in self.repo:
            print(movie)
