class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.director = "Unknown"
        self.watched = watched


    def __repr__(self):
        return "<Movie Name {}, watched already: {}>".format(self.name, self.watched)