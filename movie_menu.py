import os
import json
from user import User

def menu():
    # Ask for users name
    usersName = input("Enter your name: ")
    # check if a file already exists for that user
    filename = "{}.txt".format(usersName)
    # if it exists, load it and welcome them
    if file_exists(filename):
        with open(filename, 'r') as filehandle:
            json_data = json.load(filehandle)
        user = User.from_json(json_data)
    # if not, create a new user object
    else:
        user = User(usersName)

    while True:
        # Give them a list of options
        user_input = input("Enter 'a' to add a movie, 's' to see a list of movies, 'm' to mark a movie as watched, 'd' to delete a movie, 'l' to see list of watched movies, 'w' to write the file, or 'q' to quit  ")

        # Add a movie
        # see list of movies
        # set a movie as watched
        # delete a movie by name
        # see list of watched movies
        # save and quit
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)

        elif user_input == 's':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))

        elif user_input == 'm':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)

        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)

        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))

        elif user_input == 'w':
            with open(filename, 'w') as filehandle:
                json.dump(user.json(), filehandle)

        elif user_input == 'q':
            print("Shutting down")
            exit(1)

        else:
            print("Invalid input detected: {}, try again".format(user_input))


def file_exists(filename):
    return os.path.isfile(filename)

menu()
