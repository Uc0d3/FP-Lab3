from Repository.UserRepository import UserRepository
from Repository.MovieRepository import MovieRepository
from Controllers.UserController import UserController
from Controllers.MovieController import MovieController

from UI.UI import UI

user_repo = UserRepository()
movie_repo = MovieRepository()
user_controller = UserController(user_repo)
movie_controller = MovieController(movie_repo)

user_repo.load_from_file("users.csv")
ui = UI(user_controller, movie_controller)
ui.start()
