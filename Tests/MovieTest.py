import sys
sys.path.insert(0, "../")
from Models.User import User
from Models.Movie import Movie
from Repository.UserRepository import UserRepository
from Repository.MovieRepository import MovieRepository
from Controllers.UserController import UserController
from Controllers.MovieController import MovieController


user_repo = UserRepository()
movie_repo = MovieRepository()
user_controller = UserController(user_repo)
movie_controller = MovieController(movie_repo)

user_repo.load_from_file("users_test_data.csv")
movie_repo.load_from_file("movies_test_data.csv")


def update_price_test():
    movie = movie_controller.find_movie("1", "id", True)
    movie_controller.update_price(movie, 30)
    assert movie.price == 30
    print("Movie Update Price Test Passed")


def filter_by_rating_test():
    movies = movie_controller.filter_by_rating(8.5)
    movie = movie_controller.find_movie("2", "id", True)
    assert movies == [movie]
    print("Filter by Rating Test Passed")


def get_movies_with_actor_test():
    movies = movie_controller.get_movies_with_actor("Michael Weston")
    movie1 = movie_controller.find_movie("1", "id", True)
    movie2 = movie_controller.find_movie("2", "id", True)
    assert movies == [movie1, movie2]
    print("Get Movies with Actor Test Passed")


def run_movie_tests():
    update_price_test()
    filter_by_rating_test()
    get_movies_with_actor_test()


run_movie_tests()
