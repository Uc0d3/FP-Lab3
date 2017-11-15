class MovieRepository:

    movies = []
    last_id = 0

    def add_movie(self, movie):
        movie.set_id(self.last_id + 1)
        self.movies.append(movie)
        self.last_id += 1

    def delete_movie(self, movie):
        self.movies.remove(movie)

    def get_by_id(self, id):
        for movie in self.movies:
            if movie.id == id:
                return movie

    def __iter__(self):
        for movie in self.movies:
            yield movie
