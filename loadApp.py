from user import User
import json

with open("my_file.txt") as filehandle:
    json_data = json.load(filehandle)
    user = User.from_json(json_data)

print(user.movies)