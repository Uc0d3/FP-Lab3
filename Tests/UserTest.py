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


def change_lname_test():
    user = user_controller.find_user("1", "id", True)
    user_controller.change_lname(user, "Last Name")
    assert user.l_name == "Last Name"
    print("Change Last Name Test Passed")


def get_users_with_orders_test():
    user_with_orders = user_controller.get_users_with_orders()
    user1 = user_controller.find_user("1", "id", True)
    user2 = user_controller.find_user("2", "id", True)
    assert user_with_orders == [user1, user2]
    print("Get users with Orders Test Passed")


def add_order_test():
    movie1 = movie_controller.find_movie("1", "id", True)
    movie2 = movie_controller.find_movie("2", "id", True)
    user = user_controller.find_user("3", "id", True)
    user_controller.add_orders(user, [movie1, movie2])
    assert user.orders == [movie1.id, movie2.id]
    print("Add order Test Passed")


def run_user_tests():
    change_lname_test()
    get_users_with_orders_test()
    add_order_test()

run_user_tests()
