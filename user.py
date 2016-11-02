from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def watched_movies(self):
        watchedMovies = []
        for currentMovie in self.movies:
            if currentMovie.watched:
                watchedMovies.append(currentMovie.name)
        return watchedMovies

    def add_movie(self, name, genre):
        # create a new movie object
        newMovie = Movie(name, genre, False)
        # append it
        self.movies.append(newMovie)

    def delete_movie(self, name):
        # attempt to delete a movie named 'name'
        # by creating a new movie list
        #newMovieList = []
        #for currentMovie in self.movies:
        #    if currentMovie.name != name:
        #        newMovieList.append(currentMovie)
        #self.movies = newMovieList

        # or the super efficient method
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))


    def filter_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched

    def save_to_file(self):
        with open(self.name, 'w') as fh:
            fh.write(self.name + "\n")
            for movie in self.movies:
                fh.write("{},{},{}\n".format(movie.name, movie.genre,str(movie.watched)))

    # declare this method is for the class itself, not just an object
    @classmethod
    def load_from_file(User, filename):
        with open(filename, 'r') as fh:
            content = fh.readlines()
        username = content[0]
        print("extracted username: {}".format(username))
        movies = []
        for line in content[1:]:
            movie_data = line.split(',')
            movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
        user = User(username)
        user.movies = movies
        return user