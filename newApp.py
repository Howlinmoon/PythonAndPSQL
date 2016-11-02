from user import User
#user = User("Jim")

#user.add_movie("The Great Race", "Comedy")
#user.add_movie("Star Wars", "Sci-Fi")

#user.save_to_file()

loadedUser = User.load_from_file("Jim")

print(loadedUser.name)
print(loadedUser.movies)