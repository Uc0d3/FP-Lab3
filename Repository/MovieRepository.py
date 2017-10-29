class MovieRepository:

    movies = []
    last_id = 0


    def add_movie(self, movie):
        movie.set_id(self.last_id + 1)
        self.movies.append(movie)
        self.last_id += 1

    def get_by_id(self, id):
        for movie in self.movies:
            if movie.id == id:
                return movie

    def get_list(self):
        return self.movies
