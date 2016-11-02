from movie import Movie
from user import User
my_movie = Movie("The Great Race", "Comedy", False)

print(my_movie.genre)
print(my_movie.director)

user = User("Jim")
print(user)

user.movies.append(my_movie)

print(user.movies)

another_movie = Movie("Chitty Chitty Bang Bang", "Comedy", True)

user.movies.append(another_movie)

print(user.movies)

print("User: {} has watched: {}".format(user.name, user.watched_movies()))


# using a filter method
print("** Filter Method** User: {} has watched: {}".format(user.name, user.filter_movies()))


user.add_movie("Star Wars", "Sci-Fi")
user.add_movie("E.T.", "Lame")

print("Before deleting")
for currentMovie in user.movies:
    print("Movie Name: {}, Genre: {}".format(currentMovie.name, currentMovie.genre))

user.delete_movie("E.T.")
print("After deleting")
for currentMovie in user.movies:
    print("Movie Name: {}, Genre: {}".format(currentMovie.name, currentMovie.genre))
