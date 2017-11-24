from Models.Movie import Movie


class MovieRepository:

    movies = []
    last_id = 0
    file_name = "movies.csv"

    def __init__(self, file_name):
        self.file_name = file_name

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

    def find_movie(self, term, key=None, silent=False):
        found = []
        for movie in self.movies:
            if key is not None:
                if term.lower() in str(getattr(movie, key)).lower():
                    found.append(movie)
            else:
                members = [attr for attr in dir(movie) if not callable(getattr(movie, attr)) and not attr.startswith("__")]
                for member in members:
                    movie_prop = str(getattr(movie, member)).lower()
                    if term.lower() in movie_prop:
                        found.append(movie)
                        break
        if len(found) == 0:
            if not silent:
                print("No Movie Found")
            return None
        if len(found) == 1:
            movie = found[0]
            if not silent:
                print("Found Movies:" + str(movie))
            return movie
        if not silent:
            print("Multiple Movies Found:")
        for f_movie in found:
            if not silent:
                print(f_movie)
        if not silent:
            id = int(input("Please choose an id from the list above:"))
        return(self.get_by_id(id))

    def load_from_file(self):
        f = open(self.file_name)
        for line in f:
            try:
                data = line.split(",")
                title = data[0].strip()
                year = int(data[1].strip())
                rating = float(data[2].strip())
                price = float(data[3].strip())
                actors = data[4].strip().split(":")
                actors = list(map(str.strip, actors))
                new_movie = Movie(title, year, rating, price, actors)
                self.add_movie(new_movie)
            except IndexError as e:
                print("Corrupted user read, skipped " + str(e))
        print("Movies loaded from file")

    def save_to_file(self):
        f = open(self.file_name, "w")
        for movie in self.movies:
            csv = "%s,%d,%f,%f,%s\n"
            csv = csv % (movie.title, movie.year, movie.rating, movie.price, ":".join(movie.actors))
            f.write(csv)

    def __iter__(self):
        for movie in self.movies:
            yield movie
