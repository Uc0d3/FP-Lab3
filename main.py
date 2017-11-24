from Repository.UserRepository import UserRepository
from Repository.MovieRepository import MovieRepository
from Controllers.UserController import UserController
from Controllers.MovieController import MovieController
from UI.UI import UI

user_repo = UserRepository("users.csv")
movie_repo = MovieRepository("movies.csv")
user_controller = UserController(user_repo)
movie_controller = MovieController(movie_repo)

user_repo.load_from_file()
movie_repo.load_from_file()
ui = UI(user_controller, movie_controller)
ui.start()
