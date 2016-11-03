from user import User
import json
user = User("Jim")

user.add_movie("The Great Race", "Comedy")
user.add_movie("Star Wars", "Sci-Fi")

print(user.json())

with open('my_file.txt', 'w') as filehandle:
    json.dump(user.json(), filehandle)

#user.save_to_file()
#
#loadedUser = User.load_from_file("Jim")
#
#print(loadedUser.name)
#print(loadedUser.movies)