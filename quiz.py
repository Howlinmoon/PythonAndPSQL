class User:
    def __init__(self, name):
        self.name = name


users = [User("Jose"), User("Rolf"), User("Anna")]
selected_username = "Jose"

selected_users = list(filter(lambda user: user.name == selected_username, users))
print(selected_users[0].name)